# Write your MySQL query statement below
Select v.customer_id, count(v.customer_id) as count_no_trans
From Visits v
Where NOT EXISTS(
    select 1
    from Transactions t
    where v.visit_id = t.visit_id
)
group by v.customer_id;
