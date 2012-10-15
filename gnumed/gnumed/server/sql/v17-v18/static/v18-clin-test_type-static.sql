-- ==============================================================
-- GNUmed database schema change script
--
-- License: GPL v2 or later
-- Author: karsten.hilbert@gmx.net
--
-- ==============================================================
\set ON_ERROR_STOP 1
--set default_transaction_read_only to off;

-- --------------------------------------------------------------
-- transfer data from deprecated column
update clin.test_type
set abbrev = code
where
	abbrev is null
		and
	code is not null
;

-- --------------------------------------------------------------
-- .code
alter table clin.test_type
	drop column code cascade;


alter table audit.log_test_type
	drop column code cascade;

-- --------------------------------------------------------------
-- .coding_system
alter table clin.test_type
	drop column coding_system cascade;


alter table audit.log_test_type
	drop column coding_system;

-- --------------------------------------------------------------
select gm.log_script_insertion('v18-clin-test_type-static.sql', '18.0');
