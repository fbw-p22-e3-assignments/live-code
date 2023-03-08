\c postgres

DROP DATABASE IF EXISTS music;


CREATE DATABASE music;

\c music


CREATE TABLE musician (
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    date_of_birth TIMESTAMP,
    instrument varchar(100)
);

--Task1
insert into musician values 
    ('John', 'Lennon', '1940-10-09', 'guitar'),
    ('Paul', 'McCartney', '1942-06-18', 'bass'),
    ('George', 'Harrison', '1943-02-25', 'guitar'),
    ('Ringo', 'Starr', '1940-07-07', 'drums'),
    ('George', 'Harrison', '1943-02-25', 'guitar');
    

select * from musician;

--Task2
\i data.sql

select * from musician limit 10;

--Task3
select * from musician order by date_of_birth limit 10;
select * from musician order by date_of_birth desc limit 10;

--Task4 

select * from musician limit 5;

delete from musician where first_name = 'George' and last_name = 'Harrison'
or first_name = 'John' and last_name = 'Lennon'
or first_name = 'Paul' and last_name = 'McCartney'
or first_name = 'Ringo' and last_name = 'Starr';

select * from musician limit 5;

select * from musician order by date_of_birth desc limit 10;

--Task5
update musician set instrument='Saxophone' where instrument='Saxphone';
select * from musician where instrument='Saxophone' limit 10;

--Task6
update musician set instrument='Piano' where first_name='Bernhard' and last_name='Schwarzenegger';
select instrument from musician where first_name='Bernhard' and last_name='Schwarzenegger';

--Task7
select last_name, date_of_birth from musician where first_name='Araceli' and instrument='Piano';

--Task8
select first_name, last_name, instrument from musician where instrument='Piano' or instrument='Guitar' order by instrument, last_name limit 10;

--Task9 
select * from musician where (instrument='Piano' or instrument='Guitar') and first_name='Araceli' order by date_of_birth desc limit 3;

--Task10
select distinct instrument from musician;

--Task11
select first_name as name, last_name as "Family Name", date_of_birth as "Date of Birth" 
from musician 
where instrument='Harp' and 
        last_name like 'M%'
order by date_of_birth desc
offset 3
limit 1;

--Task12
select * from musician 
where last_name not like 'Y%' and 
        last_name not like 'M%' and 
        last_name not like 'C%' and 
        last_name not like 'A%'
order by last_name, first_name
offset 5
limit 5;

--Task13
select * from musician
where instrument in ('Guitar', 'Saxophone', 'Cello', 'Violin', 'Harp')
limit 6;

--Task14
-- truncate table musician;
select * from musician;







