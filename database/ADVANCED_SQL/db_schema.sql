create table categories(pk serial primary key, title varchar(20), description text);

insert into categories (title,description) values ('apple', 'fruits'), ('orange','fruits'),('lettuce','vegetable');

insert into categories (title) values ('lemon');

insert into categories (title,description) values ('apricot','fruits');

insert into categories (title,description) values ('tomato','vegetable');
