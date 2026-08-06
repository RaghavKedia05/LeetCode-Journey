# Write your MySQL query statement below
Select Round(
    Avg(order_date = customer_pref_delivery_date) *100
    ,2)
    as immediate_percentage
From Delivery
Where (customer_id, order_date) IN(
    Select customer_id, MIN(order_date)
    From Delivery
    Group BY customer_id
);
