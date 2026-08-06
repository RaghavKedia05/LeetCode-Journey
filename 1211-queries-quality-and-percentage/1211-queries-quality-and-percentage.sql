# Write your MySQL query statement below
Select query_name,
  Round(Sum(rating/position)/count(*),2) as quality,
  Round(Sum(Case when rating<3 Then 1 else 0 end)*100/count(rating),2) as poor_query_percentage
From Queries
Group By query_name;