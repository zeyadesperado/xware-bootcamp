# PG Exercises 

## Basic exercises
> Exercise 1 
#### *retrieve everything from a table* 

```sql
select * from cd.facilities
```
> Exercise 2 

#### Retrieve specific columns from a table
```sql
select name,membercost from cd.facilities
```

> Exercise 3 

#### Control which rows are retrieved
```sql

select * from cd.facilities where membercost > 0

```

> Exercise 4 

#### Control which rows are retrieved - part 2
```sql

select facid, name, membercost, monthlymaintenance from cd.facilities where (membercost < monthlymaintenance/50) and membercost != 0;
```

> Exercise 5

#### Basic string searches

```sql

select * from cd.facilities  where name like '%Tennis%';

```

> Exercise 6 

#### Matching against multiple possible values

```sql

select * from cd.facilities where facid in (1,5);
```
