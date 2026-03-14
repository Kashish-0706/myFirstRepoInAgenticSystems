# Importance of Structured Database in real-world AI Systems
1. Databases are important in real-world AI systems as these databases are foundational layer for AI systems. AI models required vast amounts of well-organized data for training. In real-world applications,databases ensure that data is searcheable and secure. 
Examples of data types ususally stored in databases are user's profile, transaction history, logs, labeled datasets for training, sensor data, product metadata etc.
* **Structured storage** is necessary because it enforces **consistency**, enables **indexing**, supports **efficient quering**, and also allows efficient retrieval and filtering according to requirement. * AI modes trained on these structured storage (like SQL), which leads to **more accurate outputs**.

# Relational Database Mental Model
2. The Relational model organizes data in the form of tables. These are built around clearly defined relationships between these tables.
* **Tables**: It represents one type of entity or a specific category of data.
* **Rows**: each row represents an individual record or a **unique instance** of that category.
* **Columns**: Each column represents an **attribute** (in other words, column represents properties or characteristics or type of the data).
* **Goal**: Each table should represent only one entity to avoid **data redundancy** and maintain clarity.


# Concept of Primary key
3. A Primary key is a specific column (or set of columns) which uniquely identifies each row in a table.
* **Uniqueness**: Primary keys **must be unique** because if two rows have same primary key then a specific record can't be identified.
* **Non-null**: It **can't be empty** because a record can't be identified if it's unique identifier is empty.
* **Purpose**: Primary keys  act as an **"unique address"** for the data, allowing the system to track a specific record instantly because primary keys don't have duplicates and are non- null. Without primary keys, it is impossible to reliably reference specific records.


# Database Schema
4. * **Definition**: A Database Schema is the **"blueprint"** or formal definition of how a database is organized.
* **Structure**: A schema defines **table names**, **column names**, **data types** that each column can hold (like integers, text, timestamp etc.), **constraints** (like primary keys, uniqueness).
* Schemas are important because they prevent **malformed data**, enforce **business rules**, support long-term **scalability**, ensues the structure remaons consistent as millions of records can be added easily and clean schemas reduce preprocessing complexity and data errors.


# Relationship between tables in Relational Database
5. Relational systems **normalize** data into separate tables and link them through keys. It allows data in different tables to be connected logically without repeating the information.
* **Role of Foreign key**: A foreign key is a column in one table that points to the primary key of another table. It creates a logical link between two different tables.
* **Example**: Connecting users and orders:
* The **user's table** has primary key **"user_id"**.
* The **orders table** includes a **user_id** column as foreign key.
* By matching these ids, the system knows exactly which user placed which order without having to store the user's name and address inside the "orders" table multiple times.
