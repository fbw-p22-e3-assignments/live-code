\c postgres
drop database if exists consistency;
create database consistency;
\c consistency

create table accounts(name text, balance int);

insert into accounts(name, balance) values 
    ('Newton', 3000),
    ('Columbus', 1000);

begin;
update accounts set balance = balance - 100 where name='Newton';
savepoint safe_users;
update accounts set balance = balance + 100 where name='Columbus';
commit;
