UPDATE school_records_clean
SET
    student_name = INITCAP(TRIM(student_name)),
    parent_name  = INITCAP(TRIM(parent_name));

	SELECT student_name, parent_name FROM school_records_clean LIMIT 100;
