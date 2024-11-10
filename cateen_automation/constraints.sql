select constraint_name, constraint_type
from information_schema.table_constraints
where table_name = 'users'

alter table users add constraint users_email_unique UNIQUE(email)

alter table users drop constraint users

