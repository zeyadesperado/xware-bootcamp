# Day1

## Exercise 1 - (ER diagram)

```sql
CREATE TABLE faculty(
    F_id INT PRIMARY KEY,
    F_name varchar(30) 
 );

 CREATE TABLE department(
    D_id int PRIMARY key,
    D_name varchar(30),
    F_id int
 );

 CREATE TABLE address(
    A_id int PRIMARY key,
    governorate varchar(40),
    City varchar(50),
    line_1 text not null,
    line_2 text null
 );

 CREATE TABLE Student_Address(
    Stu_A_id int PRIMARY key,
    A_id int,
    Stu_id int
 );
 CREATE TABLE Student(
    Stu_id int PRIMARY key,
    F_name varchar(30),
    L_name varchar(30),
    F_phone int,
    L_phone int,
    Birth_date date,
    image text
 );
 CREATE TABLE Professor(
    P_id int PRIMARY key,
    F_id int,
    D_id int,
    F_name varchar(30),
    L_name varchar(30),
    age char(2),
    salary float,
    image text
 );
 CREATE TABLE Subjects(
    sub_id int PRIMARY key,
    sub_name varchar (90),
    sub_code varchar(15),
    F_id int
 );
 CREATE TABLE Course(
    C_id int PRIMARY key,
    sub_id int,
    Duration varchar(20),
    P_id int
 );
 CREATE TABLE Course_Enrolment(
    C_E_id int PRIMARY key,
    C_id int,
    Stu_id int
 );
 CREATE TABLE Exams(
    E_id int PRIMARY key,
    C_id int,
    Date date,
    Time time,
    Duration varchar(20)
 );
```
