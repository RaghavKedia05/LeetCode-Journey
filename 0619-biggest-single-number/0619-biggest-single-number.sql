# Write your MySQL query statement below
select max(num) as num
from  (
    select num, count(num)
    From MyNumbers
    group by num
    Having count(num) = 1
    
)as s;