# Write your MySQL query statement below
Select r.contest_id,  Round((count(r.user_id))*100 / 
    (Select Count(*)
    From Users)
    ,2)as percentage
From Users u
Join Register r on u.user_id = r.user_id
Group By contest_id
Order by percentage Desc, contest_id asc;