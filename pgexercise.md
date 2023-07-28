# PG Exercises 

## Basic exercises

> Exercise 1 

#### retrieve everything from a table 

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

>  Exercise 7

#### Classify results into buckets

```sql
select name, CASE WHEN monthlymaintenance > 100 then 'expensive'
else 'cheap' 
end as cost
from cd.facilities;

```

> Exercise 8 

#### Working with dates

```sql
select memid, surname, firstname, joindate from cd.members where joindate > '2012-09-01'
```

> Exercise 9 

#### Removing duplicates, and ordering results

```sql
select distinct surname from cd.members order by surname limit 10;
```
> Exercise 10

#### Combining results from multiple queries

```sql
select surname from cd.members 
union Combining results from multiple queries
select name from cd.facilities;
```

> Exercise 11

#### Simple aggregation

```sql
select max(joindate) as lastest from cd.members; 
```

> Exercise 12

#### More aggregation
```sql
select firstname,surname,joindate from cd.members where
joindate = 
(select max(joindate) from cd.members);
```