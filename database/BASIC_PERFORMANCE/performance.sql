
\c performance

-- select name, setting from pg_settings 
-- where name like '%cpu%\_cost'
--     or name like '%page\_cost'
-- order by setting desc;

drop table if exists tenk1;
drop table if exists tenk2;
drop table if exists tenk3;
drop index if exists idx_tenk2_unique1;
drop index if exists idx_tenk2_num;

create table tenk1 (
                num int ); 
create table tenk2 (
                unique1 int unique); 
create table tenk3 (
                num int); 

\i data.sql

-- EXPLAIN SELECT * FROM tenk1;

create index idx_tenk2_unique on tenk2(num);
create index idx_tenk3_num on tenk3 using hash(num);

-- Explain SELECT * FROM tenk1 where num < 1;
-- Explain SELECT * FROM tenk1 where num = 1;
-- Explain SELECT * FROM tenk2 where unique1 < 1;
-- Explain SELECT * FROM tenk2 where unique1 = 1;
-- Explain SELECT * FROM tenk3 where num < 1;
-- Explain SELECT * FROM tenk3 where num = 1;

-- show data_directory;


-- query tuning

