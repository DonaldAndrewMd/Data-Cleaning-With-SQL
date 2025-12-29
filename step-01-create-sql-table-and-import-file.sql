CREATE TABLE raw_school_records (
  student_id TEXT,
  student_name TEXT,
  gender CHAR(1),
  class_name TEXT,
  class_teacher TEXT,
  teacher_phone TEXT,
  subject_name TEXT,
  subject_teacher TEXT,
  term_name TEXT,
  year INT,
  ca1 INT,
  ca2 INT,
  exam INT,
  total INT,
  grade TEXT,
  school_fees_paid TEXT,
  payment_date DATE,
  parent_name TEXT,
  parent_phone TEXT
);

copy raw_school_records
FROM 'C:/tmp/BFSS_MASTER_RECORD.csv'
DELIMITER ','
CSV HEADER;

SELECT * FROM raw_school_records
