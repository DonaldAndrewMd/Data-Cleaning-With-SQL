UPDATE school_records_clean
SET grade = CASE
    WHEN total >= 70 THEN 'A'
    WHEN total >= 60 THEN 'B'
    WHEN total >= 50 THEN 'C'
    ELSE 'F'
END;


SELECT student_name, subject_name, total, grade
FROM school_records_clean
WHERE
    (total >= 70 AND grade <> 'A')
 OR (total BETWEEN 60 AND 69 AND grade <> 'B')
 OR (total BETWEEN 50 AND 59 AND grade <> 'C')
 OR (total < 50 AND grade <> 'F');
