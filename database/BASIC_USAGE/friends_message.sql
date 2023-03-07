\c db_live
drop table if exists messages2;
drop table if exists messages3;
drop view if exists my_count;
drop table if exists full_name_messages;
drop view if exists full_name_messages;
drop view if exists full_name_message;
drop MATERIALIZED view if exists friend_messages;
drop table message;
drop view if exists my_friends;
drop table if exists messages;
drop table if exists friends;
create table friends (
    id serial primary key,
    name varchar(100) not null,
    created_at timestamp(0) default now(),
    updated_at timestamp(0) default now()
);

create table messages (
    id serial primary key,
    friends_id int references friends(id)
    on delete set null,
    message text not null,
    created_at timestamp(0) default now(),
    updated_at timestamp(0) default now()
);


\i friends_message_data.sql



-- select * from friends, messages
-- where friends.id = messages.friends_id
