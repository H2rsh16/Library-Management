show databases;

use library;

select * from book;

select * from students;

select * from admin;

select * from ishueedbooks;

select Bookname, ishueeddate from ishueedbooks where Bookname = "c" and ishueeddate = "08/09/2023" and studentname = "student1";

select id, Bookname, ishueeddate, returndate from ishueedbooks where studentname = 'student1';

create table admin(id int primary key not null auto_increment, name varchar(50), email varchar(70), password varchar(20));

create table students(id int primary key not null auto_increment, name varchar(50), email varchar(70), password varchar(20));

create table ishueedbooks(id int primary key not null auto_increment, studentname varchar(255), Bookname varchar(100), ishueeddate varchar(20), returndate varchar(255));

create table Book(id int primary key not null auto_increment, name varchar(50), description varchar(255), category varchar(255), author varchar(50), quantity int);

UPDATE book SET quantity = '20' WHERE name = 'C';

update book set author = "Gajanan A. Deshmukh" where name = "PHP";

select * from admin;

select * from students;

select name, email from admin where name = "Harsh Ovhal";

select name, email, password from admin where name = "Harsh Ovhal";

select name from admin where name = 'Harsh Ovhal' and email = 'admin@gmail.com';

insert into students(name, email, password) values('Student1', 'abc@gmail.com', '1111');

insert into admin(name, email, password) values('Harsh Ovhal', 'admin@gmail.com', '123');

insert into admin(name, email, password) values('Nope Snow', 'xyz@gmail.com', '000');

insert into book(name, description, category, author, quantity) values('Python', 'Python', 'Programming', 'Manisha Bharambe', 20),
('C', 'C programming', 'Programming', 'Manisha Bharambe', 20),
('Core Java', 'Java programming', 'Programming', 'Manisha Bharambe', 20),
('Advance Java', 'Advance Java programming', 'Programming', 'Nikhil H. Deshpande', 20),
('CPP', 'Advance C programming', 'Programming', 'Manisha Bharambe', 20),
('PHP', 'Hypertext Preprocessor', 'Programming', 'Gajanan A. Deshmukh', 20),
('Node JS', 'Javscript Framework(Node.Js)', 'Programming', 'Shivendu Bhushan', 20),
('Angular JS', 'Javascript Framework(Angular.js)', 'Programming', 'Gajanan A. Deshmukh', 20),
('Android Programming', 'Android Development', 'Programming', 'Kamil Ajmal Khan', 20);

DELETE FROM ishueedbooks WHERE Bookname = "C";

DELETE FROM ishueedbooks WHERE studentname = "student1";
insert into book(name, author, category, description, quantity) values('{n}', '{a}', '{c}', '{d}', 1);