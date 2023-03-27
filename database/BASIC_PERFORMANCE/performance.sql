\c postgres

drop database if exists performance;

create database performance;

\c performance

select name, setting from pg_settings 
where name like '%cpu%\_cost'
    or name like '%page\_cost'
order by setting desc;

create table tenk1 (
                unique1 int unique); 

\i data.sql

EXPLAIN SELECT * FROM tenk1;