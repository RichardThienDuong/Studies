# SQL Basics (mySQL based)

---

## What is SQL

- Structed Query Language is a language that is designed for creating, reading, updating, and deleting data.
- A database is a collection of data separated out into tables, these tables will be linking to each other in a relation, a table is made up of rows and columns
- The relationships between tables is what refers to a relational database management system

## SQL Fundamentals

- Grammar :
    1. Not case sensitive but best practice to write all keywords in all caps, keywords will highlight in a specific color
    2. Semicolons shoud be at the end of every statement as best practice and sql does not recognize line breaks as it will just look for the semicolon for end
    3. we use ',' commas to separate columns when using statements in table creations
- Keywords :
    1. AUTO_INCREMENT - will auto increment the column as more rows add on
    2. NOT NULL will throw an error if the value is empty as it make for best practices for things that need values.
    3.
- Keys :
    1. Primary Key - is a field(or combination of fields) that uniquely identifies each record in a table. It  cannot contain NUL values and must contain unique values.
    2. Foreign Key - is a field(or combination of fields) in one table that uniquely indentifies a row of another table. In other words, a foreign key is used to link two tables together.
    3. Unique Key - is a set of one or more fields/columns of a table that uniquely indentify a record in a database table. It is like a primary key but it can accept only one NULL value and it cannot have duplicate values.
    4. Composite Key - also known as a compound key, is a key that consists of two or more columns to identify unique rows in a table. These columns, when taken collectively, are unique across the table,ensuring that no two rows will have the same combination of values.
    5. Candidate Key - can be any column or combination of columns that can qualify as a unique key. It is a unique identifier that could be a primary key.
    6. Super Key - is a set or one of more keys that collectively identifies a record in a database. It is an attribute (or set of attributes) that can be used to identify the records uniquely.
    7. Secondary Key (or Alternate Key) - also known as alternate keys, are used mainly for data retrieval purposes. They are non-unique fields not selected as the primary keys.
- Best Practices :
    1. Almost every table in the database should have an ID column for unique identifiers
    2.

## Statement Examples

- CREATE DATABASE database_name;
- DROP DATABASE database_name;  must be sure before using this , it will delete all data!!!
- USE database_name;  will activate it for use
- CREATE TABLE table_name (
    column_name INT <!-- need to tell what type of data it holds, best practice in upper case
);
- ALTER TABLE table_name
  ADD column_name VARCHAR(255); <!-- string type of maximum 255 characters -->
- CREATE TABLE bands (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);
<!-- auto_increment will increment the number automatically for id column, the not null will throw an error if a band does not have a name. best practice to make sure every band has a name -->
- CREATE TABLE albums (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    release_year INT,
    band_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (band_id) REFERENCES bands(id) <!-- this will make -->
);
- INSERT INTO bands (name)
  VALUES ('Deuce'), ('Avenged Sevenfold'), ('Andor');
this will add to our bands table
- SELECT \* FROM bands; <!-- this will select \* (all) columns from bands and show you -->
- SELECT \* FROM bands LIMIT 2; <!-- this is select all columns but limit to only two rows -->
- SELECT name FROM bands; <!-- this will select all in names column only -->
- SELECT id AS 'ID' name AS 'Band Name' <!-- this will cause alias for id and name and can reference in future -->
  From bands;
- SELECT * FROM bands ORDER BY name; <!-- orders the rows by name -->
- SELCET * FROM bands ORDER BY name DESC; <!-- orders same thing but descending order -->
- INSERT INTO albums (name, release_year, band_id)
  VALUES ('The Number of the Beasts', 1985, 1),
         ('Power Slave', 1984, 1),
         ('Nightmare', 2018, 2),
         ('Nightmare', 2010, 3),
         ('Test Album', NULL, 3); <!-- example of inserting in mutiple things with id reference -->
- SELECT DISTINCT name FROM albums; <!-- only unique names from albums table -->

<!-- this updates info -->
UPDATE albums
SET release_year = 1982
WHERE id = 1;

<!-- selects all from albums before release_year of 2000 -->
SELECT \* FROM albums
WHERE release_year < 2000;

<!-- can search like regex and use OR keyword for other things -->
SELECT \* FROM albums
WHERE name LIKE '%er%' OR band_id = 2;

<!-- can use AND keyword as well -->
SELECT \* FROM albums
WHERE release_year = 1984 AND band_id = 1;

<!-- using BETWEEN and AND keywords -->
SELECT \* FROM albums
WHERE release_year BETWEEN 2000 AND 2018;

<!-- null searching -->
SELECT \* FROM albums
WHERE release_year IS NULL;

<!-- becareful what you use with DELETE -->
DELETE FROM albums WHERE id = 5;

<!-- JOIN feature is powerful with INNER, LEFT, RIGHT, -->
SELECT * FROM bands
JOIN albums ON bands.id = albums.band_id;

SELECT * FROM bands
RIGHT JOIN bands ON bands.id = albums.band_id;

SELECT * FROM albums
RIGHT JOIN bands ON bands.id = albums.band_id;

<!-- using math with AVG, SUM, & COUNT -->
SELECT SUM(release_year) FROM albums;
SELECT AVG(release_year) FROM albums;
SELECT band_id, COUNT(band_id) FROM albums
GROUP BY band_id;

<!-- selecting b.name as a keyword and naming it band_name for alias even tho b is not defined yet,
     then counting what a.id is and naming it as num_albums even tho a is not defined yet,
     then relating bands table we have and setting it to b as variable,
     then left joining sequence on albums table but then setting albums as a variable,
     then then saying we want to join it ON the bands table id which is the b variable .id,
     and saying b.id is equal to the albums table .band_id so it matches what to join,
     then we need to group them by b.id so we can get those aggregates to aggragate over,
      -->
SELECT b.name AS band_name, COUNT(a.id) AS num_albums
FROM bands AS b
LEFT JOIN albums AS a ON b.id = a.band_id
WHERE b.name = 'Deuce'
GROUP BY b.id
HAVING nam_albums = 1;

## Understandings

- RDBMS is The Relational Database Management Systems , which is just a database of tables that consists of rows and columns, which was made to improve redundancy
- and typically a RDBMS has a language for handling the data which is SQL
- drawsql.app is good website for visualization of tables and databases
- there are relations between tables like one to one or one to many
- a Schema is a blueprint or bird's eye view of the relations between databases
- notice a table is like a dictionary with keys and values connected with them
- there are many datatypes assigned to a key or value but they are mainly made up of strings or integers
- notice every table has an id with the primary key constraint, so it cannot be null and every row on every table can be identified
- unique id's are essential when building relationships between tables like one to one or one to many.
- each table is a unique entity that is sorted into its places accordingly, separating them into tables is just more organized and reduces actions and data rendering
