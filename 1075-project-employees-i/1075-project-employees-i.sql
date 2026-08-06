# Write your MySQL query statement below
Select p.project_id, Round(Sum(e.experience_years)/ count(p.project_id),2) as average_years
From Project p
Join Employee e on p.employee_id = e.employee_id
Group By p.project_id;
