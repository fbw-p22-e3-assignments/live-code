-- SET max_parallel_workers_per_gather = 0;
-- SHOW max_parallel_workers_per_gather;
Explain select * from posts order by created_on;

Explain analyze select * from posts order by created_on;

create index idx_posts_date on posts (created_on);
drop index if exists idx_posts_date;

select pg_size_pretty(pg_relation_size('posts')) as table_size,
pg_size_pretty(pg_relation_size('idx_posts_date'));

Explain select p.title, u.username 
from posts p
join users u on u.pk = p.author
where u.username = 'user-12';