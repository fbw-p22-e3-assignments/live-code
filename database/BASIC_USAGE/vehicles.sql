\c postgres
drop database if exists vehicles;
--Task1
create database vehicles;

\c vehicles;

/* create table car_model ( */
/*     name varchar(50), */
/*     make varchar(50), */
/*     year_of_checking varchar(4), */
/*     stock int */
/* ); */

--Task2
-- varchar(n) variable length with limit n
--char(n) exact length n (blank padded)
--TEXT no limit
create table car_model (
    name varchar(100),
    make varchar(100),
    year_of_checking varchar(4),
    engine_type varchar(10),
    stock int
);

--Task3
alter table car_model add column number_of_doors int;

\d car_model;

--Task4
alter table car_model rename column year_of_checking to year_of_manufacture;

\d car_model;

--Task5
alter table car_model 
    alter column year_of_manufacture type int
    USING year_of_manufacture::integer;

\d car_model;

--Task6
alter table car_model
    drop column year_of_manufacture;

\d car_model;



