# CREATE: Creates a new database, table, view, index, or other database objects.
CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    age INT
);

# ALTER: Modifies the structure of a table or other database objects.
ALTER TABLE students ADD COLUMN grade CHAR(1);

# DROP: Deletes a database, table, view, or other database objects.
DROP TABLE students;

# TRUNCATE: Deletes all the rows from a table, but keeps the table structure intact.
TRUNCATE TABLE students;

# RENAME: Renames a table or other database objects.
RENAME TABLE students TO new_students;

# DML (Data Manipulation Language) Commands:
# SELECT: Retrieves data from one or more tables.
SELECT * FROM students;

# INSERT: Inserts new rows into a table.
INSERT INTO students (id, name, age) VALUES (1, 'John', 20);

# UPDATE: Modifies existing data in a table.
UPDATE students SET age = 21 WHERE id = 1;

# DELETE: Deletes specific rows from a table.
DELETE FROM students WHERE id = 1;

# MERGE: Combines INSERT, UPDATE, and DELETE operations into a single statement based on specified conditions.
MERGE INTO students USING new_data ON students.id = new_data.id
WHEN MATCHED THEN
    UPDATE SET students.name = new_data.name
WHEN NOT MATCHED THEN
    INSERT (id, name, age) VALUES (new_data.id, new_data.name, new_data.age);

