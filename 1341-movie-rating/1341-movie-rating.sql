# Write your MySQL query statement below
(Select u.name as results
From Users u 
Join MovieRating mr on u.user_id = mr.user_id
Group By u.user_id
Order by count(*) desc, u.name asc
LIMIT 1)

UNION ALL

(Select m.title as results
From Movies m
Join MovieRating mr on m.movie_id = mr.movie_id
where created_at Like '2020-02%'
Group By m.movie_id
order by avg(mr.rating) desc, m.title asc
Limit 1);