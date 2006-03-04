-- Projekt GnuMed
-- Impfkalender der Firma Wyeth Lederle f�r Prevenar (Pneumokokken)

-- Quellen: Beipackzettel

-- author: Karsten Hilbert <Karsten.Hilbert@gmx.net>
-- license: GPL
-- $Source: /home/ncq/Projekte/cvs2git/vcs-mirror/gnumed/gnumed/server/sql/country.specific/de/Impfplan-Prevenar.sql,v $
-- $Revision: 1.12 $
-- =============================================
-- force terminate + exit(3) on errors if non-interactive
\set ON_ERROR_STOP 1
--delete from lnk_vaccination_definition2course;
--delete from clin.vaccination_definition;
--delete from clin.vaccination_course;

----------------------------
-- Kinder unter 6 Monaten --
----------------------------
-- Impfplan erstellen
insert into clin.vaccination_course
	(fk_recommended_by, fk_indication, comment)
values (
	-1,
	(select id from clin.vacc_indication where description='pneumococcus'),
	'Start <6 Monate, Hersteller'
);

-- Impfzeitpunkte definieren
insert into clin.vaccination_definition
	(fk_course, seq_no, min_age_due, max_age_due, comment)
values (
	currval('clin.vaccination_course_pk_seq'),
	1,
	'2 months'::interval,
	'6 months'::interval,
	'<6 Monate, Hersteller'
);

insert into clin.vaccination_definition
	(fk_course, seq_no, min_age_due, max_age_due, min_interval, comment)
values (
	currval('clin.vaccination_course_pk_seq'),
	2,
	'3 months'::interval,
	'7 months'::interval,
	'4 weeks'::interval,
	'<6 Monate, Hersteller'
);

insert into clin.vaccination_definition
	(fk_course, seq_no, min_age_due, max_age_due, min_interval, comment)
values (
	currval('clin.vaccination_course_pk_seq'),
	3,
	'4 months'::interval,
	'8 months'::interval,
	'4 weeks'::interval,
	'<6 Monate, Hersteller'
);

insert into clin.vaccination_definition
	(fk_course, seq_no, min_age_due, max_age_due, min_interval, comment)
values (
	currval('clin.vaccination_course_pk_seq'),
	4,
	'1 year'::interval,
	'2 years'::interval,
	'8 months'::interval,
	'<6 Monate, Hersteller'
);

--------------------------------------
-- Kinder zwischen 7 und 11 Monaten --
--------------------------------------
-- Impfplan erstellen
insert into clin.vaccination_course
	(fk_recommended_by, fk_indication, comment)
values (
	-1,
	(select id from clin.vacc_indication where description='pneumococcus'),
	'Start 7-11 Monate, Hersteller'
);

-- Impfzeitpunkte definieren
insert into clin.vaccination_definition
	(fk_course, seq_no, min_age_due, max_age_due, comment)
values (
	currval('clin.vaccination_course_pk_seq'),
	1,
	'7 months'::interval,
	'11 months'::interval,
	'7-11 Monate, Hersteller'
);

insert into clin.vaccination_definition
	(fk_course, seq_no, min_age_due, max_age_due, min_interval, comment)
values (
	currval('clin.vaccination_course_pk_seq'),
	2,
	'8 months'::interval,
	'12 months'::interval,
	'4 weeks'::interval,
	'7-11 Monate, Hersteller'
);

insert into clin.vaccination_definition
	(fk_course, seq_no, min_age_due, max_age_due, min_interval, comment)
values (
	currval('clin.vaccination_course_pk_seq'),
	3,
	'1 year'::interval,
	'2 years'::interval,
	'4 weeks'::interval,
	'7-11 Monate, Hersteller'
);

---------------------------------------
-- Kinder zwischen 12 und 23 Monaten --
---------------------------------------
-- Impfplan erstellen
insert into clin.vaccination_course
	(fk_recommended_by, fk_indication, comment)
values (
	-1,
	(select id from clin.vacc_indication where description='pneumococcus'),
	'Start 12-23 Monate, Hersteller'
);

-- Impfzeitpunkte definieren
insert into clin.vaccination_definition
	(fk_course, seq_no, min_age_due, max_age_due, comment)
values (
	currval('clin.vaccination_course_pk_seq'),
	1,
	'12 months'::interval,
	'23 months'::interval,
	'12-23 Monate, Hersteller'
);

insert into clin.vaccination_definition
	(fk_course, seq_no, min_age_due, max_age_due, min_interval, comment)
values (
	currval('clin.vaccination_course_pk_seq'),
	2,
	'14 months'::interval,
	'25 months'::interval,
	'2 month'::interval,
	'12-23 Monate, Hersteller'
);

-- =============================================
-- do simple revision tracking
delete from gm_schema_revision where filename like '%Impfplan-Prevenar%';
INSERT INTO gm_schema_revision (filename, version) VALUES('$RCSfile: Impfplan-Prevenar.sql,v $', '$Revision: 1.12 $');

-- =============================================
-- $Log: Impfplan-Prevenar.sql,v $
-- Revision 1.12  2006-03-04 16:24:39  ncq
-- - adjust to table name changes
--
-- Revision 1.11  2005/11/25 15:07:28  ncq
-- - create schema "clin" and move all things clinical into it
--
-- Revision 1.10  2005/09/19 16:38:52  ncq
-- - adjust to removed is_core from gm_schema_revision
--
-- Revision 1.9  2005/07/14 21:31:43  ncq
-- - partially use improved schema revision tracking
--
-- Revision 1.8  2004/04/14 13:33:04  ncq
-- - need to adjust min_interval for seq_no=1 after tightening interval checks
--
-- Revision 1.7  2004/03/18 09:56:12  ncq
-- - is_booster removal
--
-- Revision 1.6  2003/12/29 15:58:32  uid66147
-- - name cleanup
--
-- Revision 1.5  2003/12/01 22:14:24  ncq
-- - improve wording
--
-- Revision 1.4  2003/11/28 08:15:57  ncq
-- - PG 7.1/pyPgSQL/mxDateTime returns 0 for interval=1 month,
--   it works with interval=4 weeks, though, so use that
--
-- Revision 1.3  2003/11/26 23:54:51  ncq
-- - lnk_vaccdef2reg does not exist anymore
--
-- Revision 1.2  2003/11/26 00:12:19  ncq
-- - fix fk_recommended_by value
--
-- Revision 1.1  2003/11/26 00:10:45  ncq
-- - Prevenar
--
