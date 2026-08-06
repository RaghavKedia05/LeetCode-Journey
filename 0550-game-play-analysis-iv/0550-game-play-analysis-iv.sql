# Write your MySQL query statement below
Select round(
    count(distinct player_id)/ 
    (Select count(distinct 
    player_id) from activity),2) as fraction
From Activity
Where (player_id, event_date) IN
    (Select player_id, min(event_date) + interval 1 day
    From Activity
    Group By player_id);
