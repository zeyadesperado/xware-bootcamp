            
# DAY3

### Database task
> 1- Select Subject id, Subject Name, Subject Code, Course Duration in One Query

```sql

select Subjects.sub_id,Subjects.sub_name,Subjects.sub_code,course.Duration 
from Subjects
join course 
on Subjects.sub_id = course.sub_id; 

```

> 2- Select Subject id, Subject Name, Subject Code, Course Duration, Professor First_name, Professor Last_name, in One Query

```sql

select  Subjects.sub_id,Subjects.sub_name,Subjects.sub_code,course.Duration,Professor.F_name,Professor.L_name 
from Subjects 
full outer join course
on Subjects.sub_id = course.sub_id
full outer join Professor
on course.P_id = Professor.P_id;
```
> 3 - Select All Students With Thier Address In one Query

```sql 
select student.F_name,student.L_name,address.line_1
from student
left outer join Student_Address
on
 student.Stu_id = Student_Address.Stu_id
left outer join address
on
 address.A_id = Student_Address.A_id;

```

> 4- Select All Student Name In Every Couse.

```sql
select student.F_name,student.L_name , Subjects.sub_code,Subjects.sub_name
from student
inner join department
on 
student.D_id = department.D_id
inner join Subjects
on
department.D_id = Subjects.D_id
inner join course
on
Subjects.sub_id = course.sub_id;
 
 ```