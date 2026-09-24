-- 1 DISPLAY THOSE WHO REPORTS TO MANAGER_ID 100 , 124 OR 149
select * from employees where manager_id in (100, 124, 149);

-- 2 DISPLAY OTHER THAN THOSE WHO WORKS IN DEPARTMENT 90,110,10
select * from employees where DEPARTMENT_ID not in (90,110,10);

-- 3 DISPLAY ALL OTHER THAN THOSE WHO REPORTS TO 124 , 149 AND 100.
select * from employees where MANAGER_ID not in (124,149,100);

-- 4 DISPLAY FIRST_NAME AND JOB_ID WHO WORKS AS ANY OF ST_CLERK , AD_VP , SA_REP
select first_name, job_id from employees where JOB_ID in ('ST_CLERK' , 'AD_VP' , 'SA_REP');

-- 5 DISPLAY LAST_NAME , DEPARTMENT_ID , JOB_ID WHO WORKS IN AND AS 50,ST_CLERK , 80,SA_REP.
select last_name, department_id, job_id from employees where (department_id = 50 and job_id = 'st_clerk') or (department_id = 80 and job_id = 'sa_rep');

-- 6 DISPLAY ALL OTHER THAN THOSE WHO WORKS IN DEPARTMENT_ID , MANAGER_ID 60,103  80,149   110,101
select * from employees where (department_id, manager_id) not in ((60,103), (80,149), (110,101));

-- 7 DISPLAY LAST_NAME , DEPARTMENT_ID , JOB_ID , MANAGER_ID WHO WORKS WITH : 50,ST_CLERK,124    60,IT_PROG,103
select last_name, department_id, job_id, manager_id from employees where (department_id, job_id, manager_id) in ((50,'st_clerk',124), (60,'it_prog',103));

-- 8 DISPLAY THOSE WHOSE (DEPARTMENT_ID,MANAGER_ID,JOB_ID) ARE 50,124,ST_CLERK   60,103,IT_PROG    90,100,AD_VP
select * from employees where (department_id, manager_id, job_id) in ((50,124,'ST_CLERK'), (60,103,'IT_PROG'), (90,100,'AD_VP'));

-- 9 DISPLAY THOSE WHOSE FIRST_NAME CONTAINS o
select * from employees where lower(first_name) like '%o%';

-- 10 DISPLAY THOSE WHO WERE HIRED IN YEAR 98  
select * from employees where extract(year from hire_date) = 1998;

-- 11 DISPLAY THOSE WHO WERE HIRED IN ANY OF THE JAN , JUN OR JUL MONTHS
select * from employees where extract(month from hire_date) in (1,6,7);