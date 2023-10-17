# SQL README

## What's a Database?

A database is a structured collection of data that is organized and stored for efficient retrieval and manipulation. Databases are used to manage, store, and query data in various applications, from simple personal tasks to complex business operations.

## What's a Relational Database?

A relational database is a specific type of database that organizes data into tables with rows and columns. It follows the principles of relational theory, where data is structured using relationships between tables, primarily through keys like primary keys and foreign keys. This approach provides a powerful way to manage structured data and maintain data integrity.

## What Does SQL Stand For?

SQL stands for **Structured Query Language**. It's a domain-specific language used for managing and querying relational databases. SQL allows you to interact with the database to create, retrieve, update, and delete data.

## What's MySQL?

MySQL is an open-source relational database management system (RDBMS). It is one of the most popular RDBMS systems and is widely used for various applications, from small-scale projects to large enterprise-level systems. MySQL uses SQL as its query language.

## How to Create a Database in MySQL

To create a database in MySQL, you can use the following SQL command:

```sql
CREATE DATABASE database_name;
```

## What Does DDL and DML Stand For?

- **DDL**: Data Definition Language. It is a subset of SQL used for defining the structure of a database, such as creating tables, altering tables, and defining constraints.

- **DML**: Data Manipulation Language. It is a subset of SQL used for querying and modifying data in a database, including operations like inserting, updating, and deleting records.

## How to CREATE or ALTER a Table

To create a table in MySQL, use the `CREATE TABLE` statement. For example:

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
```

To alter an existing table, you can use the `ALTER TABLE` statement with various options to add, modify, or delete columns.

## How to SELECT Data from a Table

To retrieve data from a table in MySQL, use the `SELECT` statement. Here's a basic example:

```sql
SELECT column1, column2
FROM table_name
WHERE condition;
```

## How to INSERT, UPDATE, or DELETE Data

- To insert data into a table, use the `INSERT` statement.
- To update data in a table, use the `UPDATE` statement.
- To delete data from a table, use the `DELETE` statement.

## What Are Subqueries?

Subqueries (also known as subselects) are SQL queries embedded within another query. They are used to retrieve data that will be used as part of the main query. Subqueries can be placed in the `WHERE`, `SELECT`, or `FROM` clause of a SQL statement.

## How to Use MySQL Functions

MySQL provides a wide range of built-in functions for various operations, such as mathematical calculations, string manipulations, date and time handling, and more. You can use these functions in SQL statements to transform and process data as needed.

For detailed information on MySQL functions, refer to the official MySQL documentation.
