# Write your MySQL query statement below
select s.machine_id, round(avg(e.timestamp-s.timestamp),3) as processing_time
From Activity s
Join Activity e on s.machine_id = e.machine_id and s.process_id = e.process_id
Where s.activity_type ='start' and e.activity_type = 'end'
Group By s.machine_id;

    