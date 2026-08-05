# Write your MySQL query statement below
Select e.unique_id, e1.name
From Employees e1
Left Join EmployeeUNI e On e1.id = e.id;
