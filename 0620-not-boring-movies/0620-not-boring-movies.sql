# Write your MySQL query statement below
Select *
From Cinema 
Where id%2 != 0 and description!='Boring'
Order By rating desc;