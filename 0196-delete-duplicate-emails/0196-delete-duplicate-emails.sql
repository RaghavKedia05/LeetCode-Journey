# Write your MySQL query s
Delete p1
From Person p1
Join Person p2 on p1.email = p2.email
Where p1.id>p2.id;
