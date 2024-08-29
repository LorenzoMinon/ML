import sqlite3

connection = sqlite3.Connection('mydata.db') # Create a connection to the database

cursor = connection.cursor() # Create a cursor object

# cursor.execute(""" 
# CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER
# )
# """) # Create a table if it doesn't exist

# connection.commit() # Commit the changes

# #How do i open the connection on sqllite3? 

# cursor.execute("""
# INSERT INTO users(name, age) VALUES
# ('Alice', 25),
# ('Bob', 30),
# ('Charlie', 35)
# """) # Insert a row into the table

# connection.commit() # Commit the changes

# cursor.execute("""
# SELECT * FROM users
# """) # Select all rows from the table
# connection.commit() # Commit the changes


# print(cursor.execute(""" select * from users""").fetchall()) # Fetch all rows from the table


 
class Person: # Create a class Person
    def __init__(self, id_number=-1, first="",last="", age = -1): # Constructor method that initializes the attributes of the
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.Connection('mydata.db') # Create a connection to the database
        self.cursor = connection.cursor() # Create a cursor object

    def load_person(self, id_number):
        self.cursor.execute("""
        SELECT * FROM users WHERE id = {}
        """.format(id_number)) # Select a row from the table    

        results = cursor.fetchone() # Fetch the first row from the result
        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]

p1 = Person ()
p1.load_person(1)
print(p1.first, p1.last, p1.age) # Output: Alice 25