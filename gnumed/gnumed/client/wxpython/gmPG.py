#!/usr/bin/python
#############################################################################
#
# gmConnectionPool - Broker for Postgres distributed backend connections
# ---------------------------------------------------------------------------
#
# @author: Dr. Horst Herb
# @copyright: author
# @license: GPL (details at http://www.gnu.org)
# @dependencies: pg, gmLoginInfo
# @change log:
#	25.10.2001 hherb first draft, untested
#	29.10.2001 hherb crude functionality achieved (works ! (sortof))
#	30.10.2001 hherb reference counting to prevent disconnection of active connections
#	==========================================================================
#	significant version change!
#	==========================================================================
#	08.02.2002 hherb made DB API 2.0 compatible.
#
# @TODO: Almost everything
############################################################################

#python standard modules
import string, gettext, copy, os, sys
#3rd party dependencies
import pgdb
#gnumed specific modules
import gmLoginInfo, gmLog, gmExceptions

#take care of translating strings
_ = gettext.gettext

#create an alias for our DB API adapter module to make code independend of the adapter used
dbapi = pgdb
__backend = 'Postgres'
#check whether this adapter module suits our needs
assert(float(dbapi.apilevel) >= 2.0)
assert(dbapi.threadsafety > 0)
assert(dbapi.paramstyle == 'pyformat') 



class ConnectionPool:
	"maintains a static dictionary of available database connections"

	#a dictionary with lists of databases; dictionary key is the name of the database
	__databases = {}
	__connections_in_use = {}
	__connected = None


	def __init__(self, login=None):
		"parameter login is of type gmLoginInfo.LoginInfo"
		if login is not None:
			self.__disconnect()
		if ConnectionPool.__connected is None:
			ConnectionPool.__connected = self.__connect(login)


	def __connect(self, login):
		"initialize connection to all neccessary servers"

		if login==None and ConnectionPool.__connected is None:
			try:
				login = inputLoginParams()
			except:
				raise gmExceptions.ConnectionError(_("Can't connect to database without login information!"))

		#first, connect to the configuration server
		try:
			cdb = self.__pgconnect(login)
		except:
			raise gmExceptions.ConnectionError(_("Could not connect to configuration database  backend!"))

		ConnectionPool.__connected = 1

		#this is the default gnumed server now!
		ConnectionPool.__databases['config'] = cdb
		ConnectionPool.__databases['default'] = cdb

		#try to establish connections to all servers we need
		#according to configuration database
		cursor = cdb.cursor()
		cursor.execute("select * from config where profile='%s'" %
		            login.GetProfile())
		databases = cursor.fetchall()
		dbidx = cursorIndex(cursor)

		#for all configuration entries that match given user and profile
		for db in databases:

			###get the symbolic name of the distributed service
			cursor.execute("select name from distributed_db where id = %d" %  db[dbidx['ddb']])
			service = string.strip(cursor.fetchone()[0])
			print "processing service " , service

			###initialize our reference counter
			ConnectionPool.__connections_in_use[service]=0

			###try to get login information for a particular service
			querystr = "select name, host, port, opt, tty from db where id = %d" % db[dbidx['db']]
			cursor.execute(querystr)
			database = cursor.fetchone()
			idx = cursorIndex(cursor)

			###create a copy of the default login information, keeping user name and password
			dblogin = copy.deepcopy(login)
			###get the name of the distributed datbase service
			try:
				dblogin.SetDatabase(string.strip(database[idx['name']]))
			except: pass
			###hostname of the distributed service
			try:
				dblogin.SetHost(string.strip(database[idx['host']]))
			except: pass
			###port of the distributed service
			try:
				dblogin.SetPort(database[idx['port']])
			except: pass
			###backend options of the distributed service
			try:
				dblogin.SetOptions(string.strip(database[idx['opt']]))
			except: pass
			###TTY option of the distributed service
			try:
				dblogin.SetTTY(string.strip(database[idx['tty']]))
			except:pass
			#update 'Database Broker' dictionary
			ConnectionPool.__databases[service] = self.__pgconnect(dblogin)
		try:
		    cursor.close()
		except:
		    pass

		return ConnectionPool.__connected



	### private method
	def __pgconnect(self, login):
		"connect to a postgres backend as specified by login object; return a connection object"
		
		dsn, hostport = login.GetPGDB_DSN()
		try:
		    db = pgdb.connect(dsn, host=hostport)
		    return db
		except: 
		    self.LogError(_("Connection to database failed. \nDSN was [%s], host:port was [%s]") % (dsn, hostport))
		    raise gmExceptions.ConnectionError, _("Connection to database failed. \nDSN was [%s], host:port was [%s]") % (dsn, hostport)




	def __decrypt(self, crypt_pwd, crypt_algo, pwd):
		"""decrypt the encrypted password crypt_pwd using the stated algorithm
		and the given password pwd"""
		#TODO!!!
		pass


	def __disconnect(self, force_it=0):
		"safe disconnect (respecting possibly active connections) unless the force flag is set"
		###are we conected at all?
		if ConnectionPool.__connected is None:
			###just in case
			ConnectionPool.__databases.clear()
			return
		###disconnect from all databases
		for key in ConnectionPool.__databases.keys():
			### check whether this connection might still be in use ...
			if ConnectionPool.__connections_in_use[service] > 0 :
				###unless we are really mean :-(((
				if force_it == 0:
					#let the end user know that shit is happening
					raise gmExceptions.ConnectionError, \
					    _("Attempting to close a database connection that is still in use")
			else:
				###close the connection
				ConnectionPool.__databases[key].close()

		#clear the dictionary (would close all connections anyway)
		ConnectionPool.__databases.clear()
		ConnectionPool.__connected = None



	def GetConnection(self, service):
		"if a distributed service exists, return it - otherwise return the default server"
		if ConnectionPool.__databases.has_key(service):
			try:
				ConnectionPool.__connections_in_use[service] += 1
			except:
				ConnectionPool.__connections_in_use[service] = 1
			return ConnectionPool.__databases[service]
		else:
			try:
				ConnectionPool.__connections_in_use['default'] += 1
			except:
				ConnectionPool.__connections_in_use['default'] = 1

			return ConnectionPool.__databases['default']



	def ReleaseConnection(self, service):
		"decrease reference counter of active connection"
		if ConnectionPool.__databases.has_key(service):
			try:
				ConnectionPool.__connections_in_use[service] -= 1
			except:
				ConnectionPool.__connections_in_use[service] = 0
		else:
			try:
				ConnectionPool.__connections_in_use['default'] -= 1
			except:
				ConnectionPool.__connections_in_use['default'] = 0



	def GetAvailableServices(self):
		"""list all distributed services available on this system
		(according to configuration database)"""
		return ConnectionPool.__databases.keys()

	def Connected(self):
		return ConnectionPool.__connected

	def LogError(self, msg):
		"This function must be overridden by GUI applications"
		print msg


### database helper functions

def cursorIndex(cursor):
    "returns a dictionary of row atribute names and their row indices"
    i=0
    dict={}
    for d in cursor.description:
	dict[d[0]] = i
	i+=1
    return dict


def descriptionIndex(cursordescription):
    "returns a dictionary of row atribute names and their row indices"
    i=0
    dict={}
    for d in cursordescription:
	dict[d[0]] = i
	i+=1
    return dict



def dictResult(cursor, fetched=None):
	"returns the all rows fetchable by the cursor as dictionary (attribute:value)"
	if fetched is None:
		fetched = cursor.fetchall()
	attr = fieldNames(cursor)
	dictres = []
	for f in fetched:
		dict = {}
		i=0
		for a in attr:
    	    		dict[a]=f[i]
		dictres.append(dict)
		i+=1
	return dictres




def fieldNames(cursor):
	"returns the attribute names of the fetched rows in natural sequence as a list"
	names=[]
	for d in cursor.description:
		names.append(d[0])
	return names


def listDatabases(service='default'):
	"list all accessible databases on the database backend of the specified service"
	assert(__backend == 'Postgres')
	return quickROQuery("select * from pg_database")

def listUserTables(service='default'):
	"list the tables except all system tables of the specified service"
	assert(__backend == 'Postgres')
	return quickROQuery("select * from pg_tables where tablename not like 'pg_%'", service)


def listSystemTables(service='default'):
	"list the system tables of the specified service"
	assert(__backend == 'Postgres')
	return quickROQuery("select * from pg_tables where tablename like 'pg_%'", service)


def listTables(service='default'):
	"list all tables available in the specified service"
	return quickROQuery("select * from pg_tables", service)


def quickROQuery(query, service='default'):
	"""a quick read-only query that fetches all possible results at once
	returns the tuple containing the fetched rows and the cursor 'description' object"""

	dbp = ConnectionPool()
	con = dbp.GetConnection(service)
	cur=con.cursor()
	cur.execute(query)
	return cur.fetchall(), cur.description



def getBackendName():
	return __backend



def inputTMLoginParams():
	"text mode input request of database login parameters"
	login = gmLoginInfo.LoginInfo('', '')
	try:
		print "\nPlease enter the required login parameters:"
		user = raw_input("user name : ")
		password = raw_input("password : ")
		database = raw_input("database [gnumed] : ")
		if database == '': database = 'gnumed'
		host = raw_input("host [localhost] : ")
		if host == '': host = 'localhost'
		port = raw_input("port [5432] : ")
		if port == '':
			port = 5432
		else:
			port = int(port)
		login.SetInfo(user, password, dbname=database, host=host, port=port)
	except:
		raise gmExceptions.ConnectionError(_("Can't connect to database without login information!"))
	return login



def inputWXLoginParams():
	"""GUI (wx) mode input request of database login parameters.
	Returns gmLoginINfo.LoginInfo object"""

	import sys
	#the next statement will raise an exception if wxPython is not loaded yet
	sys.modules['wxPython']
	#OK, wxPython was already loaded. Let's launch the login dialog
	#if wx was not initialized /no main App loop, an exception should be raised anyway
	import gmLoginDialog
	dlg = gmLoginDialog.LoginDialog(None, -1, png_bitmap = 'bitmaps/gnumedlogo.png')
	dlg.ShowModal()
	login = dlg.panel.GetLoginParams()
	#if user cancelled or something else went wrong, raise an exception
	if login is None:
		raise gmExceptions.ConnectionError(_("Can't connect to database without login information!"))
	#memory cleanup, shouldn't really be neccessary
	dlg.Destroy()
	return login


def inputLoginParams():
	"input request for database backend login parameters. Try GUI dialog if available"
	if 'DISPLAY' in os.environ.keys () or sys.platform in ["win32", "mac"]:
		try:
			login = inputWXLoginParams()
		except:
			login = inputTMLoginParams()
	else:
		login = inputTMLoginParams ()
	return login



### test function for this module: simple start as "main" module
if __name__ == "__main__":
	dbpool = ConnectionPool()
	### Let's see what services are distributed in this system:
	print "\n\nServices available on this system:"
	print '-----------------------------------------'
	for service in dbpool.GetAvailableServices():
		print service
		dummy=dbpool.GetConnection(service)
		print "Available tables within service: ", service
		tables, cd = listUserTables(service)
		idx = descriptionIndex(cd)
		for table in tables:
			print "%s (owned by user %s)" % (table[idx['tablename']], table[idx['tableowner']])
		print "\n.......................................\n"

	### We have probably not distributed the services in full:
	db = dbpool.GetConnection('config')
	print "\n\nPossible services on any gnumed system:"
	print '-----------------------------------------'
	cursor = db.cursor()
	cursor.execute("select name from distributed_db")
	for service in  cursor.fetchall():
		print service[0]

	print "\nTesting convenience funtions:\n============================\n"
	print "Databases:\n============\n"
	res, descr = listDatabases()
	for r in res: print r
	print "\nTables:\n========\n"
	res, descr = listTables()
	for r in res: print r
	print "\nResult as dictionary\n==================\n"
	cur = db.cursor()
	cursor.execute("select * from db")
	d = dictResult(cursor)
	print d
