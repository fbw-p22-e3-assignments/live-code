create table posts(pk serial primary key, 
                    title text,
                    content text,
                    author int,
                    category int);

insert into posts(title,content,author,category) values('my orange','my orange is the best orange in the world',1,2);
insert into posts(title,content,author,category) values('my apple','my apple is the best orange in the world',1,1);
insert into posts(title,content,author,category) values('Re:my orange','No! It''s my orange the best orange in the world',2,2);
insert into posts(title,content,author,category) values('my tomato','my tomato is the best orange in the world',2,6);
insert into posts (title,content,author,category) values ('my new orange','this my post on my new orange',1,2);