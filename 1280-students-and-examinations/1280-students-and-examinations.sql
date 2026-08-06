# Write your MySQL query statement below
Select s.student_id, s.student_name, s1.subject_name,
(Select Count(e.subject_name) 
From Examinations e
Where e.student_id = s.student_id AND e.subject_name = s1.subject_name) as attended_exams
From Students s
Cross join Subjects s1 
Order By s.student_id, s1.subject_name ASC;
