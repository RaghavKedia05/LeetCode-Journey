# Write your MySQL query statement below
Select(
    Select distinct salary  
From Employee
Order by salary desc
limit 1 offset 1) as SecondHighestSalary
;