# Write your MySQL query statement below
Select p.product_name, sum(o.unit) as unit 
From Products p
Join Orders o on p.product_id = o.product_id
Where order_date Between '2020-02-01' and '2020-02-29'
Group by p.product_id
Having unit>=100;