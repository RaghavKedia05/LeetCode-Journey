# Write your MySQL query statement below
Select cd.id 
From Weather cd
Join Weather pd On DateDiff(cd.recordDate, pd.recordDate) = 1
Where cd.temperature > pd.temperature;
