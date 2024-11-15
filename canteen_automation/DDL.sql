ALTER TABLE users
ADD COLUMN nickname varchar(10)

ALTER TABLE users
RENAME COLUMN nickname to nick_name

ALTER TABLE users
DROP COLUMN nick_name

ALTER TABLE table_name
ADD COLUMN column_name
MODIFY COLUMN 
RENAME COLUMN 
DROP COLUMN

ALTER TABLE users RENAME TO customers
ALTER TABLE customers RENAME TO users