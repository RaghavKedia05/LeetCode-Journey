# Write your MySQL query statement below
Select t.request_at as Day, 
    round(sum(case when t.status='cancelled_by_driver' then 1
        when t.status='cancelled_by_client' then 1 else 0 end)/count(*),2) as 'Cancellation Rate'
From Trips t
Join Users u on t.client_id = u.users_id
Join Users u1 on t.driver_id = u1.users_id
Where u.banned = 'No' and 
    u1.banned = 'No'
    and t.request_at Between '2013-10-01' and '2013-10-03'
Group By request_at 
Order By request_at ASC;