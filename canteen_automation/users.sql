drop table users cascade delete

CREATE TABLE users(
user_id SERIAL PRIMARY KEY, 
role_id int REFERENCES roles(role_id) ON DELETE SET NULL, 
username varchar(50) NOT NULL,
password varchar(100), 
full_name varchar(100),
email varchar(100), 
contact_number varchar(15), 
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from roles
select * from users

INSERT INTO users (role_id, username, password, full_name, email, contact_number)
VALUES
(1, 'admin1', 'admin1', 'Admin One', 'admin1@test.com', '09964557349'),
(2, 'user1', 'user1', 'User One', 'user1@test.com', '09975587831')
