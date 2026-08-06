# Write your MySQL query statement below
Select p.product_id , Round(IFNULL((SUM(p.price*u.units))/ Sum(u.units),0),2) as average_price
From Prices p
Left Join UnitsSold u ON p.product_id = u.product_id 
and u.purchase_date >= p.start_date and u.purchase_date<= p.end_date
Group by p.product_id;