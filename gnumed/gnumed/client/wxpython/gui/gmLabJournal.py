"""
"""
#============================================================================
# $Source: /home/ncq/Projekte/cvs2git/vcs-mirror/gnumed/gnumed/client/wxpython/gui/gmLabJournal.py,v $
__version__ = ""
__author__ = "Sebastian Hilbert <Sebastian.Hilbert@gmx.net>"

# system
import os.path, sys, os, re
# FIXME: debugging
import time

from Gnumed.pycommon import gmLog
_log = gmLog.gmDefLog

if __name__ == '__main__':
	_log.SetAllLogLevels(gmLog.lData)
	from Gnumed.pycommon import gmI18N
else:
	from Gnumed.pycommon import gmGuiBroker

_log.Log(gmLog.lData, __version__)

from Gnumed.pycommon import gmPG, gmCfg, gmExceptions, gmWhoAmI, gmMatchProvider
from Gnumed.business import gmPatient, gmClinicalRecord, gmPathLab
from Gnumed.wxpython import gmGuiHelpers, gmPhraseWheel
from Gnumed.pycommon.gmPyCompat import *
from Gnumed.wxpython import checkboxOn, checkboxOff, imagestest
# 3rd party
from wxPython.wx import *
from wxPython.lib.mixins.listctrl import wxColumnSorterMixin, wxListCtrlAutoWidthMixin

_cfg = gmCfg.gmDefCfgFile
_whoami = gmWhoAmI.cWhoAmI()

[   wxID_PNL_main,
	wxID_NB_LabJournal,
	wxID_LBOX_pending_results,
	wxID_PHRWH_labs,
	wxID_TXTCTRL_ids,
	wxID_BTN_save_request_ID
] = map(lambda _init_ctrls: wxNewId(), range(6))

class cLabWheel(gmPhraseWheel.cPhraseWheel):
	def __init__(self, parent):
		query = """
			select pk, internal_name
			from test_org
			"""
		self.mp = gmMatchProvider.cMatchProvider_SQL2('historica', query)
		self.mp.setThresholds(aWord=2, aSubstring=4)

		gmPhraseWheel.cPhraseWheel.__init__(
			self,
			parent = parent,
			id = -1,
			aMatchProvider = self.mp,
			size = wxDefaultSize,
			pos = wxDefaultPosition
		)
		self.SetToolTipString(_('choose which lab will process the probe with the specified ID'))
#====================================
class gmLabIDListCtrl(wxListCtrl, wxListCtrlAutoWidthMixin):
	#BEGIN_EVENT_TABLE(gmLabIDListCtrl, wxListCtrl)
	#	EVT_LEFT_DOWN(gmLabIDListCtrl, self.OnMouseEvent)
	#END_EVENT_TABLE()
	
	def __init__(self, parent, ID, pos=wxDefaultPosition, size=wxDefaultSize, style=0):
		wxListCtrl.__init__(self, parent, ID, pos, size, style)
		wxListCtrlAutoWidthMixin.__init__(self)
		
	def AppendColouredItem(self, sLabel = None): 
		NewItem = wxListItem()
		NewItem.SetMask(wxLIST_MASK_TEXT);
		NewItem.SetId(self.GetItemCount());
		NewItem.SetText(sLabel);
		NewItem.SetFont(wxITALIC_FONT);
		NewItem.SetTextColour(wxRED);
		NewItem.SetBackgroundColour(wxColour(235, 235, 235));

		#self.InsertItem(NewItem)
		#return NewItem
#====================================
class cLabJournalNB(wxNotebook):
	"""This wxNotebook derivative displays 'records still due' and lab-import related errors.
	"""
	def __init__(self, parent, id):
		"""Set up our specialised notebook.
		"""
		# connect to config database
		pool = gmPG.ConnectionPool()
		self.__dbcfg = gmCfg.cCfgSQL(
			aConn = pool.GetConnection('default'),
			aDBAPI = gmPG.dbapi
		)
		
		wxNotebook.__init__(
			self,
			parent,
			id,
			wxDefaultPosition,
			wxDefaultSize,
			0
		)
		# tab with pending requests
		self.PNL_due_tab = wxPanel( self, -1 )
		szr_due = self.__init_SZR_due()

		self.PNL_due_tab.SetAutoLayout( True )
		self.PNL_due_tab.SetSizer( szr_due )
		szr_due.Fit( self.PNL_due_tab )
		szr_due.SetSizeHints(self.PNL_due_tab)

		self.AddPage( self.PNL_due_tab, _("pending results"))

		# tab with errors
		self.PNL_errors_tab = wxPanel( self, -1)
		szr_errors = self.__init_SZR_import_errors()

		self.PNL_errors_tab.SetAutoLayout( True )
		self.PNL_errors_tab.SetSizer( szr_errors )
		szr_errors.Fit( self.PNL_errors_tab )
		szr_errors.SetSizeHints( self.PNL_errors_tab )

		self.AddPage( self.PNL_errors_tab, _("lab errors"))
		
		# tab with unreviewed lab results
		self.PNL_review_tab = wxPanel( self, -1)
		szr_review = self.__init_SZR_review_status()

		self.PNL_review_tab.SetAutoLayout( True )
		self.PNL_review_tab.SetSizer( szr_review )
		szr_review.Fit( self.PNL_review_tab )
		szr_review.SetSizeHints( self.PNL_review_tab )

		self.AddPage( self.PNL_review_tab, _("unreviewed results"))
		
		self.curr_pat = gmPatient.gmCurrentPatient()
	#------------------------------------------------------------------------
	def __init_SZR_due (self):

		vbszr = wxBoxSizer( wxVERTICAL )
		hbszr = wxBoxSizer( wxHORIZONTAL )
		
		self.lab_label = wxStaticText(
			name = 'lablabel',
			parent = self.PNL_due_tab,
			id = -1,
			label = _('Lab')
		)
		
		# available labs go here
		self.lab_wheel = cLabWheel(self.PNL_due_tab)
		self.lab_wheel.on_resize (None)
		self.lab_wheel.addCallback(self.on_lab_selected)

		hbszr.AddWindow(self.lab_label, 0, wxALIGN_CENTER | wxALL, 5)
		hbszr.AddWindow(self.lab_wheel, 0, wxALIGN_CENTER | wxALL, 5)
		
		vbszr.AddWindow(hbszr,0, wxALIGN_LEFT | wxALL, 5)
		
		self.req_id_label = wxStaticText(
			name = 'req_id_label',
			parent = self.PNL_due_tab,
			id = -1,
			label = _("Specimen ID")
		)
		
		# request_id field
		self.fld_request_id = wxTextCtrl(
			self.PNL_due_tab,
			wxID_TXTCTRL_ids,
			"",
			wxDefaultPosition,
			wxSize(80,-1),
			0
			)

		hbszr2 = wxBoxSizer( wxHORIZONTAL )
		
		hbszr2.AddWindow(self.req_id_label, 0, wxALIGN_CENTER | wxALL, 5)
		hbszr2.AddWindow(self.fld_request_id, 0, wxALIGN_CENTER| wxALL, 5 )
		
		vbszr.AddWindow(hbszr2,0, wxALIGN_LEFT | wxALL, 5)

		# -- "save request id" button -----------
		self.BTN_save_request_ID = wxButton(
			name = 'BTN_save_request_ID',
			parent = self.PNL_due_tab,
			id = wxID_BTN_save_request_ID,
			label = _("save request ID")
		)
		self.BTN_save_request_ID.SetToolTipString(_('associate chosen lab and ID with current patient'))
		EVT_BUTTON(self.BTN_save_request_ID, wxID_BTN_save_request_ID, self.on_save_request_ID)

		vbszr.AddWindow( self.BTN_save_request_ID, 0, wxALIGN_CENTER|wxALL, 5 )

		# our actual list
		tID = wxNewId()
		self.lbox_pending = gmLabIDListCtrl(
			self.PNL_due_tab,
			tID,
			size=wxDefaultSize,
			style=wxLC_REPORT|wxSUNKEN_BORDER|wxLC_VRULES
		)

		self.lbox_pending.InsertColumn(0, _("date"))
		self.lbox_pending.InsertColumn(1, _("lab"))
		self.lbox_pending.InsertColumn(2, _("sample id"))
		self.lbox_pending.InsertColumn(3, _("patient"))
		self.lbox_pending.InsertColumn(4, _("status"))
		
		vbszr.AddWindow( self.lbox_pending, 1, wxEXPAND|wxALIGN_CENTER|wxALL, 5 )
		return vbszr

	def __init_SZR_import_errors (self):
		vbszr = wxBoxSizer( wxVERTICAL )

		tID = wxNewId()
		self.lbox_errors = gmLabIDListCtrl(
			self.PNL_errors_tab,
			tID,
			size=wxDefaultSize,
			style=wxLC_REPORT|wxSUNKEN_BORDER|wxLC_VRULES
		)

		vbszr.AddWindow(self.lbox_errors, 1, wxEXPAND| wxALIGN_CENTER | wxALL, 5)

		self.lbox_errors.InsertColumn(0, _("noticed when"))
		self.lbox_errors.InsertColumn(1, _("problem"))
		self.lbox_errors.InsertColumn(2, _("solution"))
		self.lbox_errors.InsertColumn(3, _("context"))
		return vbszr

	def __init_SZR_review_status (self):
		vbszr = wxBoxSizer( wxVERTICAL )
		tID = wxNewId()
		
		self.review_Ctrl = gmLabIDListCtrl(
			self.PNL_review_tab,
			tID,
			size=wxDefaultSize,
			style=wxLC_REPORT|wxSUNKEN_BORDER|wxLC_VRULES
		)
		
		# image list for panel
		self.il = wxImageList(16, 16)
		self.idx1 = self.il.Add(imagestest.getSmilesBitmap())
		self.review_Ctrl.SetImageList(self.il, wxIMAGE_LIST_SMALL)

		vbszr.AddWindow(self.review_Ctrl, 1, wxEXPAND | wxALIGN_CENTER | wxALL, 5)

		self.review_Ctrl.InsertColumn(0, _(" "))
		self.review_Ctrl.InsertColumn(1, _("patient name"))
		self.review_Ctrl.InsertColumn(2, _("dob"))
		self.review_Ctrl.InsertColumn(3, _("date"))
		self.review_Ctrl.InsertColumn(4, _("analysis"))
		self.review_Ctrl.InsertColumn(5, _("result"))
		self.review_Ctrl.InsertColumn(6, _("range"))
		self.review_Ctrl.InsertColumn(7, _("info provided by lab"))
		
		return vbszr
	#------------------------------------------------------------------------
	def OnLeftDClick(self, evt):
		pass
		
	#------------------------------------------------------------------------
	def update(self):
		if self.curr_pat['ID'] is None:
			_log.Log(gmLog.lErr, 'need patient for update, no patient related notebook tabs will be visible')
			gmGuiHelpers.gm_show_error(
				aMessage = _('Cannot load lab journal.\nYou first need to select a patient.'),
				aTitle = _('loading lab journal')
			)
			return None

		if self.__populate_notebook() is None:
			return None
		return 1
	#------------------------------------------------------------------------
	def __populate_notebook(self):
		
		self.fld_request_id.Clear()
		self.lab_wheel.Clear()
		self.lbox_pending.DeleteAllItems()
		#------ due PNL ------------------------------------
		# FIXME: make limit configurable
		too_many, pending_requests = gmPathLab.get_pending_requests(limit=250)
		# FIXME: make use of too_many
		for request in pending_requests:
			item_idx = self.lbox_pending.InsertItem(info=wxListItem())
			# request date
			self.lbox_pending.SetStringItem(index = item_idx, col=0, label=request['clin_when'].date)
			# request lab
			lab = self.__get_labname(request['fk_test_org'])
			self.lbox_pending.SetStringItem(index = item_idx, col=1, label=lab[0][0])
			# request id
			self.lbox_pending.SetStringItem(index = item_idx, col=2, label=request['request_id'])
			# patient name
			name, dobobj = self.__get_pat4result(request)
			self.lbox_pending.SetStringItem(index = item_idx, col=3, label=name)
			self.lbox_pending.SetStringItem(index = item_idx, col=4, label=_('pending'))
			# FIXME: make use of rest data in patient via mouse over context
		#----- import errors PNL -----------------------
		lab_errors = self.__get_import_errors()
		for lab_error in lab_errors:
			item_idx = self.lbox_errors.InsertItem(info=wxListItem())
			# when was error reported
			self.lbox_errors.SetStringItem(index = item_idx, col=0, label=lab_error[1].date)
			# error
			self.lbox_errors.SetStringItem(index = item_idx, col=1, label=lab_error[4])
			# solution
			self.lbox_errors.SetStringItem(index = item_idx, col=2, label=lab_error[5])
			# context
			self.lbox_errors.SetStringItem(index = item_idx, col=3, label=lab_error[6])
		#------ unreviewed lab results PNL ------------------------------------
		#t1 = time.time()
		# FIXME: make configurable
		more_avail, data = gmPathLab.get_unreviewed_results(limit=50)
		#t2 = time.time()
		#print t2-t1
		if more_avail is None:
			item_idx = self.review_Ctrl.InsertItem(info=wxListItem())
			item = self.review_Ctrl.GetItem(item_idx)
			item.SetTextColour(wxRED)
			self.review_Ctrl.SetItem(item)
			self.review_Ctrl.SetStringItem(index = item_idx, col=2, label=data)
			return None

		for result in data:
			item_idx = self.review_Ctrl.InsertItem(info=wxListItem())
			
			# -- put checkbox in first column
			self.review_Ctrl.InsertImageItem(index = item_idx, imageIndex=self.idx1)
			self.review_Ctrl.SetColumnWidth(0, wxLIST_AUTOSIZE)

			# abnormal ? -> display in red
			if (result['abnormal'] is not None) and (result['abnormal'].strip() != ''):
				item = self.review_Ctrl.GetItem(item_idx)
				item.SetTextColour(wxRED)
				self.review_Ctrl.SetItem(item)
			# patient name
			name, dobobj = self.__get_pat4result(result)
			self.review_Ctrl.SetStringItem(index = item_idx, col=1, label=name)
			self.review_Ctrl.SetStringItem(index = item_idx, col=2, label=dobobj.date)
			# when rxd
			self.review_Ctrl.SetStringItem(index = item_idx, col=3, label=result['lab_rxd_when'].date)
			# test name
			self.review_Ctrl.SetStringItem(index = item_idx, col=4, label=result['unified_name'])
			# result including unit
			# FIXME: what about val_unit empty ?
			self.review_Ctrl.SetStringItem(item_idx, 5, '%s %s' % (result['unified_val'], result['val_unit']))
			# normal range
			if not result['val_normal_range'] is None:
				self.review_Ctrl.SetStringItem(index = item_idx, col=6, label=result['val_normal_range'])
			else:
				self.review_Ctrl.SetStringItem(index = item_idx, col=6, label='')
			# notes from provider 
			if not result['note_provider'] is None:
				self.review_Ctrl.SetStringItem(index = item_idx, col=7, label=result['note_provider'])
			else:
				self.review_Ctrl.SetStringItem(index = item_idx, col=7, label='')

		# we show 50 items at once , notify user if there are more
		if more_avail:
			#self.review_Ctrl.GetItemCount()
			item_idx = self.review_Ctrl.InsertItem(info=wxListItem())
			self.review_Ctrl.SetStringItem(index= item_idx, col=6, label=_('more results available for review'))
	#------------------------------------------------------------------------
	def __get_import_errors(self):
		query = """select * from housekeeping_todo where category='lab'"""
		import_errors = gmPG.run_ro_query('historica', query)
		return import_errors
	#------------------------------------------------------------------------
	def __get_labname(self, data):
		query= """select internal_name from test_org where pk=%s"""
		labs = gmPG.run_ro_query('historica', query, None, data)
		return labs
	#------------------------------------------------------------------------
	def __get_last_used_ID(self, lab_name):
		query = """
			select request_id 
			from lab_request lr0 
			where lr0.clin_when = (
				select max(lr1.clin_when)
				from lab_request lr1 
				where lr1.fk_test_org = ( 
					select pk 
					from test_org 
					where internal_name=%s 
				)
			)"""
		last_id = gmPG.run_ro_query('historica', query, None, lab_name)
		return last_id
	#--------------------------------------------------------------------------	
	def guess_next_id(self, lab_name):
	
		if not len(self.__get_last_used_ID(lab_name)) == 0:
			last = self.__get_last_used_ID(lab_name)[0][0]
			next = chr(ord(last[-1:])+1)
			return next
		else:
			return None
	#--------------------------------------------------------------------------
	def __get_pat4result(self,result):
		pat4result = result.get_patient()
		#query = """select * from v_basic_person where i_id=%s"""
		#pat4result = gmPG.run_ro_query('historica', query, None, id)
		#return pat4result[0][4]+' '+pat4result[0][5], pat4result[0][6]
		return pat4result[2]+' '+pat4result[3], pat4result[4]
	#-----------------------------------
	# event handlers
	#-----------------------------------
	def on_save_request_ID(self, event):
		req_id = self.fld_request_id.GetValue()
		if not req_id is None or req_id == '':
			emr = self.curr_pat.get_clinical_record()
			if emr is None:
				# FIXME: error message
				return None
			test = gmPathLab.create_lab_request(lab=self.lab_name[0][0], req_id = req_id, pat_id = self.curr_pat['ID'], encounter_id = emr.id_encounter, episode_id= emr.id_episode)
			#test = gmPathLab.create_lab_request(req_id='ML#SC937-0176-CEC#11', lab='Enterprise Main Lab', encounter_id = emr.id_encounter, episode_id= emr.id_episode)
			# react on succes or failure of save_request
			print test
		else :
			_log.Log(gmLog.lErr, 'No request ID typed in yet !')
			gmExceptions.gm_show_error (
				_('You must type in a request ID !\n\nUsually you will find the request ID written on\nthe barcode sticker on your probe container.'),
				_('saving request id')
			)
			return None
		self.__populate_notebook()
	#--------------------------------------------------------
	def __on_right_click(self, evt):
		#pass
		evt.Skip()
	#-------------------------------------------------------
	def on_lab_selected(self,data):
		if data is None:
			self.fld_request_id.SetValue('')

		print "phrase wheel just changed lab to", data
		# get last used id for lab
		self.lab_name = self.__get_labname(data)
		print self.lab_name
		#guess next id
		nID = self.guess_next_id(self.lab_name[0][0])
		if not nID is None:
			# set field to that
			self.fld_request_id.SetValue(nID)
#== classes for standalone use ==================================
if __name__ == '__main__':

	print "let's work on the plugin version only for now"

#	from Gnumed.pycommon import gmLoginInfo
#	from Gnumed.business import gmXdtObjects, gmXdtMappings, gmDemographicRecord

#	wxID_btn_quit = wxNewId()

#	class cStandalonePanel(wxPanel):

#		def __init__(self, parent, id):
#			# get patient from file
#			if self.__get_pat_data() is None:
#				raise gmExceptions.ConstructorError, "Cannot load patient data."

			# set up database connectivity
#			auth_data = gmLoginInfo.LoginInfo(
#				user = _cfg.get('database', 'user'),
#				passwd = _cfg.get('database', 'password'),
#				host = _cfg.get('database', 'host'),
#				port = _cfg.get('database', 'port'),
#				database = _cfg.get('database', 'database')
#			)
#			backend = gmPG.ConnectionPool(login = auth_data)

			# mangle date of birth into ISO8601 (yyyymmdd) for Postgres
#			cooked_search_terms = {
				#'dob': '%s%s%s' % (self.__xdt_pat['dob year'], self.__xdt_pat['dob month'], self.__xdt_pat['dob day']),
#				'lastnames': self.__xdt_pat['last name'],
#				'firstnames': self.__xdt_pat['first name'],
#				'gender': self.__xdt_pat['gender']
#			}
#			print cooked_search_terms
			# find matching patient IDs
#			searcher = gmPatient.cPatientSearcher_SQL()
#			patient_ids = searcher.get_patient_ids(search_dict = cooked_search_terms)
#			if patient_ids is None or len(patient_ids)== 0:
#				gmGuiHelpers.gm_show_error(
#					aMessage = _('This patient does not exist in the document database.\n"%s %s"') % (self.__xdt_pat['first name'], self.__xdt_pat['last name']),
#					aTitle = _('searching patient')
#				)
#				_log.Log(gmLog.lPanic, self.__xdt_pat['all'])
#				raise gmExceptions.ConstructorError, "Patient from XDT file does not exist in database."

			# ambigous ?
#			if len(patient_ids) != 1:
#				gmGuiHelpers.gm_show_error(
#					aMessage = _('Data in xDT file matches more than one patient in database !'),
#					aTitle = _('searching patient')
#				)
#				_log.Log(gmLog.lPanic, self.__xdt_pat['all'])
#				raise gmExceptions.ConstructorError, "Problem getting patient ID from database. Aborting."

#			try:
#				gm_pat = gmPatient.gmCurrentPatient(aPKey = patient_ids[0])
#			except:
				# this is an emergency
#				gmGuiHelpers.gm_show_error(
#					aMessage = _('Cannot load patient from database !\nAborting.'),
#					aTitle = _('searching patient')
#				)
#				_log.Log(gmLog.lPanic, 'Cannot access patient [%s] in database.' % patient_ids[0])
#				_log.Log(gmLog.lPanic, self.__xdt_pat['all'])
#				raise

			# make main panel
#			wxPanel.__init__(self, parent, id, wxDefaultPosition, wxDefaultSize)
#			self.SetTitle(_("lab journal"))

			# make patient panel
#			gender = gmDemographicRecord.map_gender_gm2long[gmXdtMappings.map_gender_xdt2gm[self.__xdt_pat['gender']]]
#			self.pat_panel = wxStaticText(
#				id = -1,
#				parent = self,
#				label = "%s %s (%s), %s.%s.%s" % (self.__xdt_pat['first name'], self.__xdt_pat['last name'], gender, self.__xdt_pat['dob day'], self.__xdt_pat['dob month'], self.__xdt_pat['dob year']),
#				style = wxALIGN_CENTER
#			)
#			self.pat_panel.SetFont(wxFont(25, wxSWISS, wxNORMAL, wxNORMAL, 0, ""))

			# make lab journal notebook 
#			self.nb = cLabJournalNB(self, -1)
#			self.nb.update()

			# buttons
#			btn_quit = wxButton(
#				parent = self,
#				id = wxID_btn_quit,
#				label = _('Quit')
#			)
#			EVT_BUTTON (btn_quit, wxID_btn_quit, self.__on_quit)
			
#			szr_buttons = wxBoxSizer(wxHORIZONTAL)
#			szr_buttons.Add(btn_quit, 0, wxALIGN_CENTER_VERTICAL, 1)

#			szr_main = wxBoxSizer(wxVERTICAL)
#			szr_main.Add(self.pat_panel, 0, wxEXPAND, 1)
#			szr_nb = wxNotebookSizer( self.nb )
			
#			szr_main.Add(szr_nb, 1, wxEXPAND, 9)
#			szr_main.Add(szr_buttons, 0, wxEXPAND, 1)

#			self.SetAutoLayout(1)
#			self.SetSizer(szr_main)
#			szr_main.Fit(self)
#			self.Layout()
		#--------------------------------------------------------
#		def __get_pat_data(self):
		#	"""Get data of patient for which to retrieve documents.

		#	"""
			# FIXME: error checking
#			pat_file = os.path.abspath(os.path.expanduser(_cfg.get("viewer", "patient file")))
			# FIXME: actually handle pat_format, too
#			pat_format = _cfg.get("viewer", "patient file format")

			# get patient data from BDT file
#			try:
#				self.__xdt_pat = gmXdtObjects.xdtPatient(anXdtFile = pat_file)
#			except:
#				_log.LogException('Cannot read patient from xDT file [%s].' % pat_file, sys.exc_info())
#				gmGuiHelpers.gm_show_error(
#					aMessage = _('Cannot load patient from xDT file\n[%s].') % pat_file,
#					aTitle = _('loading patient from xDT file')
#				)
#				return None

#			return 1
		#--------------------------------------------------------
#		def __on_quit(self, evt):
#			app = wxGetApp()
#			app.ExitMainLoop()

#== classes for plugin use ======================================
else:

	class cPluginPanel(wxPanel):
		def __init__(self, parent, id):
			# set up widgets
			wxPanel.__init__(self, parent, id, wxDefaultPosition, wxDefaultSize)

			# make lab notebook
			self.nb = cLabJournalNB(self, -1)
			
			# just one vertical sizer
			sizer = wxBoxSizer(wxVERTICAL)
			szr_nb = wxNotebookSizer( self.nb )
			
			sizer.Add(szr_nb, 1, wxEXPAND, 0)
			self.SetAutoLayout(1)
			self.SetSizer(sizer)
			sizer.Fit(self)
			self.Layout()
		#--------------------------------------------------------
		def __del__(self):
			# FIXME: return service handle
			#self.DB.disconnect()
			pass

	#------------------------------------------------------------
	from Gnumed.wxpython import gmPlugin, images_Archive_plugin, images_Archive_plugin1

	class gmLabJournal(gmPlugin.wxNotebookPlugin):
		tab_name = _("lab journal")

		def name (self):
			return gmLabJournal.tab_name

		def GetWidget (self, parent):
			self.panel = cPluginPanel(parent, -1)
			return self.panel

		def MenuInfo (self):
			return ('tools', _('Show &lab journal'))

		def ReceiveFocus(self):
			if self.panel.nb.update() is None:
				_log.Log(gmLog.lErr, "cannot update lab journal with data")
				return None
			# FIXME: register interest in patient_changed signal, too
			#self.panel.tree.SelectItem(self.panel.tree.root)
			self.DoStatusText()
			return 1

		def can_receive_focus(self):
			# need patient
			if not self._verify_patient_avail():
				return None
			return 1

		def DoToolbar (self, tb, widget):
			
			tb.AddControl(wxStaticBitmap(
				tb,
				-1,
				images_Archive_plugin.getvertical_separator_thinBitmap(),
				wxDefaultPosition,
				wxDefaultSize
			))
			
		def DoStatusText (self):
			# FIXME: people want an optional beep and an optional red backgound here
			#set_statustext = gb['main.statustext']
				txt = _('how are you doing today ?') 
				if not self._set_status_txt(txt):
					return None
				return 1
#================================================================
# MAIN
#----------------------------------------------------------------
if __name__ == '__main__':
	_log.Log (gmLog.lInfo, "starting lab journal")

	if _cfg is None:
		_log.Log(gmLog.lErr, "Cannot run without config file.")
		sys.exit("Cannot run without config file.")

	# catch all remaining exceptions
	try:
		application = wxPyWidgetTester(size=(640,480))
		application.SetWidget(cStandalonePanel,-1)
		application.MainLoop()
	except:
		_log.LogException("unhandled exception caught !", sys.exc_info(), 1)
		# but re-raise them
		raise
	#gmPG.StopListeners()
	_log.Log (gmLog.lInfo, "closing lab journal")
else:
	# we are being imported
	pass
#================================================================
# $Log: gmLabJournal.py,v $
# Revision 1.15  2004-05-26 11:07:04  shilbert
# - gui layout changes
#
# Revision 1.14  2004/05/25 13:26:49  ncq
# - cleanup
#
# Revision 1.13  2004/05/25 08:15:20  shilbert
# - make use of gmPathLab for db querries
# - introduce limit for user visible list items
#
# Revision 1.12  2004/05/22 23:29:09  shilbert
# - gui updates (import error context , ctrl labels )
#
# Revision 1.11  2004/05/18 20:43:17  ncq
# - check get_clinical_record() return status
#
# Revision 1.10  2004/05/18 19:38:54  shilbert
# - gui enhancements (wxExpand)
#
# Revision 1.9  2004/05/08 17:43:55  ncq
# - cleanup here and there
#
# Revision 1.8  2004/05/06 23:32:45  shilbert
# - now features a tab with unreviewed lab results
#
# Revision 1.7  2004/05/04 09:26:55  shilbert
# - handle more errors
#
# Revision 1.6  2004/05/04 08:42:04  shilbert
# - first working version, needs testing
#
# Revision 1.5  2004/05/04 07:19:34  shilbert
# - kind of works, still a bug in create_request()
#
# Revision 1.4  2004/05/01 10:29:46  shilbert
# - custom event handlig code removed, pending lab ids input almost completed
#
# Revision 1.3  2004/04/29 21:05:19  shilbert
# - some more work on auto update of id field
#
# Revision 1.2  2004/04/28 16:12:02  ncq
# - cleanups, as usual
#
# Revision 1.1  2004/04/28 07:20:00  shilbert
# - initial release after name change, lacks features
#
