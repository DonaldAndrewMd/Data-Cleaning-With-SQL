UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'Adeye', 'Adeoye');

UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'Adoye', 'Adeoye');
UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'Momo', 'Momoh');

UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'Momohh', 'Momoh');

UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'Momorr', 'Momoh');
UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'Okayke', 'Okeke');

UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'Okeka', 'Okeke');

UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'Okike', 'Okeke');
UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'Danladil', 'Danladi');

UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'Danlady', 'Danladi');

UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'Dalandi', 'Danladi');
UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'Adebyo', 'Adebayo');

UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'Adebayi', 'Adebayo');

UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'Adebay', 'Adebayo');


UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'Mister ', 'Mr ');

UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'Mr. ', 'Mr ');

UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'MR ', 'Mr ');

UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'mr ', 'Mr ');

UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'Misses ', 'Mrs ');

UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'Mrs. ', 'Mrs ');

UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'MRS ', 'Mrs ');

UPDATE school_records_clean
SET parent_name = REPLACE(parent_name, 'mrs ', 'Mrs ');


SELECT DISTINCT parent_name
FROM school_records_clean
ORDER BY parent_name
