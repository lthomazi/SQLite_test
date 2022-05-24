import os
import sqlite3

# Delete existing database
os.remove("gta.db")

# create an empty database
connection = sqlite3.connect("gta.db")
# create object to communicate with the database
cursor = connection.cursor()

try:
    # create a table with three columns (and their types)
    cursor.execute("create table gta(release_year integer, release_name text, city text)")

    # create a tuple 
    release_list = [
        (1997, "Grand Theft Auto", "state of New Guernsey"),
        (1999, "Grand Theft Auto 2", "Anywhere, USA"),
        (2001, "Grand Theft Auto III", "Liberty City"),
        (2002, "Grand Theft Auto: Vice City", "Vice City"),
        (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
        (2008, "Grand Theft Auto IV", "Liberty City"),
        (2013, "Grand Theft Auto V", "Los Santos")
    ]

    # insert into database a tuple with three values
    cursor.executemany("insert into gta values (?,?,?)", release_list)
except:
    print("Data base exists")


# print data to verify insertion
for row in cursor.execute("select * from gta"):
    print(row)

# print specific row/value
# select all from gta where the column of city will be represented by the dictionary key
# of 'c', followed by the dictionary itself where the key of 'c' corresponds to the 
# value of liberty city
cursor.execute("select * from gta where city=:c", {"c": "Liberty City"})
gta_city_search = cursor.fetchall()
print("Target = liberty city: ", gta_city_search)

# search for the name game released in 2013
cursor.execute("select release_name from gta where release_year=:y", {"y": "2013"})
gta_year_search = cursor.fetchall()
print("Released in 2013: ", gta_year_search)

# change all instances of Liberty City to Los Angeles
for i in gta_city_search:
    adjusted = ["Los Angeles" if value == "Liberty City" else value for value in i]
    print(adjusted)

# terminate connection
connection.close()