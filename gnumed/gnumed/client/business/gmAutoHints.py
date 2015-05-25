# -*- coding: utf-8 -*-
"""GNUmed auto hints middleware.

This should eventually end up in a class cPractice.
"""
#============================================================
__license__ = "GPL"
__author__ = "K.Hilbert <Karsten.Hilbert@gmx.net>"


import sys
import logging


if __name__ == '__main__':
	sys.path.insert(0, '../../')
from Gnumed.pycommon import gmPG2
from Gnumed.pycommon import gmBusinessDBObject
from Gnumed.pycommon import gmTools
from Gnumed.pycommon import gmDateTime

from Gnumed.business import gmStaff

_log = logging.getLogger('gm.hints')

#============================================================
# dynamic hints API
#------------------------------------------------------------
_SQL_get_dynamic_hints = u"SELECT * FROM ref.v_auto_hints WHERE %s"

class cDynamicHint(gmBusinessDBObject.cBusinessDBObject):
	"""Represents dynamic hints to be run against the database."""

	_cmd_fetch_payload = _SQL_get_dynamic_hints % u"pk_auto_hint = %s"
	_cmds_store_payload = [
		u"""UPDATE ref.auto_hint SET
				query = gm.nullify_empty_string(%(query)s),
				recommendation_query = gm.nullify_empty_string(%(recommendation_query)s),
				title = gm.nullify_empty_string(%(title)s),
				hint = gm.nullify_empty_string(%(hint)s),
				url = gm.nullify_empty_string(%(url)s),
				source = gm.nullify_empty_string(%(source)s),
				is_active = %(is_active)s
			WHERE
				pk = %(pk_auto_hint)s
					AND
				xmin = %(xmin_auto_hint)s
			RETURNING
				xmin AS xmin_auto_hint
		"""
	]
	_updatable_fields = [
		u'query',
		u'recommendation_query',
		u'title',
		u'hint',
		u'url',
		u'source',
		u'is_active'
	]
	#--------------------------------------------------------
	def format(self):
		txt = u'%s               [#%s]\n' % (
			gmTools.bool2subst(self._payload[self._idx['is_active']], _('Active clinical hint'), _('Inactive clinical hint')),
			self._payload[self._idx['pk_auto_hint']]
		)
		txt += u'\n'
		txt += self._payload[self._idx['title']]
		txt += u'\n'
		txt += u'\n'
		txt += _('Source: %s\n') % self._payload[self._idx['source']]
		txt += _('Language: %s\n') % self._payload[self._idx['lang']]
		txt += u'\n'
		txt += gmTools.wrap(self._payload[self._idx['hint']], width = 50, initial_indent = u' ', subsequent_indent = u' ')
		txt += u'\n'
		txt += u'\n'
		if self._payload[self._idx['recommendation']] is not None:
			txt += gmTools.wrap(self._payload[self._idx['recommendation']], width = 50, initial_indent = u' ', subsequent_indent = u' ')
			txt += u'\n'
			txt += u'\n'
		txt += gmTools.wrap (
			gmTools.coalesce(self._payload[self._idx['url']], u''),
			width = 50,
			initial_indent = u' ',
			subsequent_indent = u' '
		)
		txt += u'\n'
		txt += u'\n'
		txt += gmTools.wrap(self._payload[self._idx['query']], width = 50, initial_indent = u' ', subsequent_indent = u' ')
		txt += u'\n'
		if self._payload[self._idx['recommendation_query']] is not None:
			txt += u'\n'
			txt += gmTools.wrap(self._payload[self._idx['recommendation_query']], width = 50, initial_indent = u' ', subsequent_indent = u' ')
			txt += u'\n'
		return txt
	#--------------------------------------------------------
	def suppress(self, rationale=None, pk_encounter=None):
		return suppress_dynamic_hint (
			pk_hint = self._payload[self._idx['pk_auto_hint']],
			pk_encounter = pk_encounter,
			rationale = rationale
		)
	#--------------------------------------------------------
	def invalidate_suppression(self, pk_encounter=None):
		return invalidate_hint_suppression (
			pk_hint = self._payload[self._idx['pk_auto_hint']],
			pk_encounter = pk_encounter
		)

#------------------------------------------------------------
def get_dynamic_hints(order_by=None, link_obj=None):
	if order_by is None:
		order_by = u'TRUE'
	else:
		order_by = u'TRUE ORDER BY %s' % order_by

	cmd = _SQL_get_dynamic_hints % order_by
	rows, idx = gmPG2.run_ro_queries(link_obj = link_obj, queries = [{'cmd': cmd}], get_col_idx = True)
	return [ cDynamicHint(row = {'data': r, 'idx': idx, 'pk_field': 'pk_auto_hint'}) for r in rows ]

#------------------------------------------------------------
def create_dynamic_hint(link_obj=None, query=None, title=None, hint=None, source=None):
	args = {
		u'query': query,
		u'title': title,
		u'hint': hint,
		u'source': source,
		u'usr': gmStaff.gmCurrentProvider()['db_user']
	}
	cmd = u"""
		INSERT INTO ref.auto_hint (
			query,
			title,
			hint,
			source,
			lang
		) VALUES (
			gm.nullify_empty_string(%(query)s),
			gm.nullify_empty_string(%(title)s),
			gm.nullify_empty_string(%(hint)s),
			gm.nullify_empty_string(%(source)s),
			i18n.get_curr_lang(%(usr)s)
		)
		RETURNING pk
	"""
	rows, idx = gmPG2.run_rw_queries(link_obj = link_obj, queries = [{'cmd': cmd, 'args': args}], return_data = True, get_col_idx = True)
	return cDynamicHint(aPK_obj = rows[0]['pk'], link_obj = link_obj)

#------------------------------------------------------------
def delete_dynamic_hint(link_obj=None, pk_hint=None):
	args = {'pk': pk_hint}
	cmd = u"DELETE FROM ref.auto_hint WHERE pk = %(pk)s"
	gmPG2.run_rw_queries(link_obj = link_obj, queries = [{'cmd': cmd, 'args': args}])
	return True

#------------------------------------------------------------
def get_hints_for_patient(pk_identity=None, include_suppressed_needing_invalidation=False):
	conn = gmPG2.get_connection()
	curs = conn.cursor()
	curs.callproc('clin.get_hints_for_patient', [pk_identity])
	rows = curs.fetchall()
	idx = gmPG2.get_col_indices(curs)
	curs.close()
	conn.rollback()
	if not include_suppressed_needing_invalidation:
		return [ cDynamicHint(row = {'data': r, 'idx': idx, 'pk_field': 'pk_auto_hint'}) for r in rows if r['rationale4suppression'] != 'magic_tag::please_invalidate_suppression' ]
	return [ cDynamicHint(row = {'data': r, 'idx': idx, 'pk_field': 'pk_auto_hint'}) for r in rows ]

#------------------------------------------------------------
def suppress_dynamic_hint(pk_hint=None, rationale=None, pk_encounter=None):
	args = {
		'hint': pk_hint,
		'rationale': rationale,
		'enc': pk_encounter
	}
	cmd = u"""
		DELETE FROM clin.suppressed_hint
		WHERE
			fk_hint = %(hint)s
				AND
			fk_encounter IN (
				SELECT pk FROM clin.encounter WHERE fk_patient = (
					SELECT fk_patient FROM clin.encounter WHERE pk = %(enc)s
				)
			)
	"""
	queries = [{'cmd': cmd, 'args': args}]
	cmd = u"""
		INSERT INTO clin.suppressed_hint (
			fk_encounter,
			fk_hint,
			rationale,
			md5_sum
		) VALUES (
			%(enc)s,
			%(hint)s,
			%(rationale)s,
			(SELECT r_vah.md5_sum FROM ref.v_auto_hints r_vah WHERE r_vah.pk_auto_hint = %(hint)s)
		)
	"""
	queries.append({'cmd': cmd, 'args': args})
	gmPG2.run_rw_queries(queries = queries)
	return True

#------------------------------------------------------------
# suppressed dynamic hints
#------------------------------------------------------------
_SQL_get_suppressed_hints = u"SELECT * FROM clin.v_suppressed_hints WHERE %s"

class cSuppressedHint(gmBusinessDBObject.cBusinessDBObject):
	"""Represents suppressed dynamic hints per patient."""

	_cmd_fetch_payload = _SQL_get_suppressed_hints % u"pk_suppressed_hint = %s"
	_cmds_store_payload = []
	_updatable_fields = []
	#--------------------------------------------------------
	def format(self):
		txt = u'%s               [#%s]\n' % (
			gmTools.bool2subst(self._payload[self._idx['is_active']], _('Suppressed active dynamic hint'), _('Suppressed inactive dynamic hint')),
			self._payload[self._idx['pk_suppressed_hint']]
		)
		txt += u'\n'
		txt += u'%s\n\n' % self._payload[self._idx['title']]
		txt += _('Suppressed by: %s\n') % self._payload[self._idx['suppressed_by']]
		txt += _('Suppressed at: %s\n') % gmDateTime.pydt_strftime(self._payload[self._idx['suppressed_when']], '%Y %b %d')
		txt += _('Hint #: %s\n') % self._payload[self._idx['pk_hint']]
		txt += _('Patient #: %s\n') % self._payload[self._idx['pk_identity']]
		txt += _('MD5 (currently): %s\n') % self._payload[self._idx['md5_hint']]
		txt += _('MD5 (at suppression): %s\n') % self._payload[self._idx['md5_suppressed']]
		txt += _('Source: %s\n') % self._payload[self._idx['source']]
		txt += _('Language: %s\n') % self._payload[self._idx['lang']]
		txt += u'\n'
		txt += u'%s\n' % gmTools.wrap(self._payload[self._idx['hint']], width = 50, initial_indent = u' ', subsequent_indent = u' ')
		txt += u'\n'
		if self._payload[self._idx['recommendation']] is not None:
			txt += u'\n'
			txt += u'%s\n' % gmTools.wrap(self._payload[self._idx['recommendation']], width = 50, initial_indent = u' ', subsequent_indent = u' ')
			txt += u'\n'
		txt += u'%s\n' % gmTools.wrap (
			gmTools.coalesce(self._payload[self._idx['url']], u''),
			width = 50,
			initial_indent = u' ',
			subsequent_indent = u' '
		)
		txt += u'\n'
		txt += u'%s\n' % gmTools.wrap(self._payload[self._idx['query']], width = 50, initial_indent = u' ', subsequent_indent = u' ')
		return txt

#------------------------------------------------------------
def get_suppressed_hints(pk_identity=None, order_by=None):
	args = {'pat': pk_identity}
	if pk_identity is None:
		where = u'true'
	else:
		where = u"pk_identity = %(pat)s"
	if order_by is None:
		order_by = u''
	else:
		order_by = u' ORDER BY %s' % order_by
	cmd = (_SQL_get_suppressed_hints % where) + order_by
	rows, idx = gmPG2.run_ro_queries(queries = [{'cmd': cmd, 'args': args}], get_col_idx = True)
	return [ cSuppressedHint(row = {'data': r, 'idx': idx, 'pk_field': 'pk_suppressed_hint'}) for r in rows ]

#------------------------------------------------------------
def delete_suppressed_hint(pk_suppressed_hint=None):
	args = {'pk': pk_suppressed_hint}
	cmd = u"DELETE FROM clin.suppressed_hint WHERE pk = %(pk)s"
	gmPG2.run_rw_queries(queries = [{'cmd': cmd, 'args': args}])
	return True

#------------------------------------------------------------
def invalidate_hint_suppression(pk_hint=None, pk_encounter=None):
	_log.debug('invalidating suppression of hint #%s', pk_hint)
	args = {
		'pk_hint': pk_hint,
		'enc': pk_encounter,
		'fake_md5': '***INVALIDATED***'			# only needs to NOT match ANY md5 sum
	}
	cmd = u"""
		UPDATE clin.suppressed_hint SET
			fk_encounter = %(enc)s,
			md5_sum = %(fake_md5)s
		WHERE
			pk = (
				SELECT pk_suppressed_hint
				FROM clin.v_suppressed_hints
				WHERE
					pk_hint = %(pk_hint)s
						AND
					pk_identity = (
						SELECT fk_patient FROM clin.encounter WHERE pk = %(enc)s
					)
			)
		"""
	gmPG2.run_rw_queries(queries = [{'cmd': cmd, 'args': args}])
	return True

#============================================================
if __name__ == '__main__':

	if len(sys.argv) < 2:
		sys.exit()

	if sys.argv[1] != 'test':
		sys.exit()

	from Gnumed.pycommon import gmI18N

	gmI18N.activate_locale()
	gmI18N.install_domain()

	#---------------------------------------
	def test_auto_hints():
#		for row in get_dynamic_hints():
#			print row
		for row in get_hints_for_patient(pk_identity = 12):
			print row
	#---------------------------------------
	test_auto_hints()