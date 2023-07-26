# Day2

### Database Task
> - Insert Data Into These Tables.
>   - Insert One Faculty
>   - Insert Three Departments Into This Faculty
>   - Insert Three Subjects In Every Department
>   - Insert Courses With Different Durations
>   - Insert At Least Five Students In Every Department
>   - Insert Exams For Every Course

```sql
-- Insert Faculty
insert into faculty values (1, 'Computer and Information');

-- Insert Departments
insert into department (D_name, F_id) values ('CS', 1), ('IT', 1), ('IS', 1);

-- Insert Subjects
insert into Subjects(sub_name, sub_code, D_id) values 
  ('Operating system', 'CS212', 1),
  ('Data Structures', 'CS213', 1),
  ('Computer Vision', 'CS214', 1),
  ('Network Programming', 'IT311', 2),
  ('Socket Programming', 'IT312', 2),
  ('Tcp Connections', 'IT313', 2),
  ('Data analysis', 'IS411', 3),
  ('IS strategy', 'IS412', 3),
  ('Database administration', 'IS413', 3);

-- Insert Professors
insert into Professor(P_id, F_id, D_id, F_name, L_name, age, salary) values
  (1, 1, 1, 'Mostafa', 'Kamel', 38, 15000),
  (2, 1, 1, 'mostafa', 'darwesh', 42, 12000),
  (3, 1, 1, 'marghany', 'Hassan', 55, 17000),
  (4, 1, 2, 'nagwa', 'omar', 39, 11000),
  (5, 1, 2, 'dalia', 'khaled', 31, 9000),
  (6, 1, 2, 'Ali', 'Hussain', 38, 13000),
  (7, 1, 3, 'Ibrahem', 'Elawdy', 42, 14500),
  (8, 1, 3, 'sara', 'Nashaat', 32, 8000),
  (9, 1, 3, 'noha', 'Elayaat', 35, 8500);

-- Insert Courses
insert into Course values (1, '3 hours', 11, 1),
  (2, '2 hours', 10, 2),
  (3, '3 hours', 12, 3),
  (4, '4 hours', 13, 4),
  (5, '3 hours', 14, 5),
  (6, '3 hours', 15, 6),
  (7, '2 hours', 16, 7),
  (8, '3 hours', 17, 8),
  (9, '4 hours', 18, 9);

-- Insert Students
insert into Student(Stu_id, F_name, L_name, D_id) values
  (1, 'ahmed', 'mohamed', 1),
  (2, 'sayed', 'mohamed', 1),
  (3, 'mostafa', 'mohamed', 1),
  (4, 'zeyad', 'mohamed', 1),
  (5, 'gamal', 'mohamed', 1),
  (6, 'gameel', 'refaat', 2),
  (7, 'emad', 'refaat', 2),
  (8, 'khaled', 'refaat', 2),
  (9, 'hesham', 'refaat', 2),
  (10, 'tarek', 'refaat', 2),
  (11, 'samer', 'ibrahem', 3),
  (12, 'ahmed', 'hamza', 3),
  (13, 'shaban', 'hamza', 3),
  (14, 'raheem', 'hamza', 3),
  (15, 'ashref', 'hamza', 3);

-- Insert Exams
insert into Exams(C_id, date, time, Duration) values 
  (1, '2023-08-15', '12:00', '2 hours'),
  (2, '2023-08-16', '11:30', '1 hour'),
  (3, '2023-08-18', '12:00', '2 hours'),
  (4, '2023-08-18', '11:30', '1 hour'),
  (5, '2023-08-20', '12:00', '2 hours'),
  (6, '2023-08-21', '11:30', '3 hours'),
  (7, '2023-08-23', '12:00', '2 hours'),
  (8, '2023-08-23', '11:30', '1 hour'),
  (9, '2023-08-24', '11:00', '3 hours');

------ select ------
select * from Student;
select * from Professor;
select * from Subjects;
select * from Course;
select * from Exams;
select * from department;
select * from Professor where age = 38;
select * from Professor where salary > 10000;
select * from Professor order by salary ASC;
select avg(salary) from Professor;
update Professor set salary = 20000 where salary > 10000;
delete from Professor where salary > 19000;
------ update -------
alter table Student add age int;
