# DataBaseManager
A simple DataBaseManager manager. You can manage DataBaseManager simply without using SQL or any other query language. The Inputs and outputs are in the form of JSON so you can simply share the data across networks. A simple SQL shell was attached to do more with Your Db.
Execute "pip install DataBaseManager"
Then import it By Executing
"import DataBaseManager"

# Supported DataBases:
1)SQLite

# multiprocess:

now (v0.0.8) supports multi processing. manage multiple databases(0-infinity)  By multiprocess object. one command to manage mulitple databases!. More info given below..

view: https://techabam.000webhsotapp.com/DbManager/

# SQLite
1)import:-
'from DataBaseManager import sqlite'
2)create object:-
'MyObj = sqlite("your file path")
3)If you want to create a new Db
'MyObj = sqlite()'
'MyObj.CreateDb("db name",{"table name":{"column":"type"}})'
4)For inserting data:-
'MyObj.insert("table name",[{"column1":"value1","column2":"value2"},{"column":"next items"}])'
5)for selecting:- 
'MyObj.select(["table1","table2"],select=["table1.column","table2.column"],where={"table1.column":"value","table2.column":"value2"}))'
This will return the data in the form of a list of the result tuples same as the form of fetchall()
Use MyObj.parse_fetch_all() to get the data in the form of dictionary
5)For Getting shell:-
"MyObj.shell('Any commands if you want')"
6)also have execute, executescript, commit, fetchone,fetchall etc. cursor same as the python sqlite3
7) execute MyObj.conn to return the connection
8) execute MyObj.schema to get the schema in the form of a dictionary
9) execute MyObj.tables to get the table names
10)to start a multiprocess:-
'from DataBaseManager import multiprocess'
'MyObj = multiprocess(your_data_base("database name"),your_second_database("databasename"))'
your data base name may be sqlite or any other DataBaseManager Supports.
execute MyObj.insert, update ,execute,executescript,select, commit, etc. as same in the other db objects
11)to start sqlite shell execute:-
'python -m DataBaseManager -sqlite file_name'
for help:- 
'python -m DataBaseManager --help'

sqlite shell info at:- https://techabam.000webhostapp.com/DataBaseManager/sqlite/shell.html
More info on the link:
https://techabam.000webhostapp.com/DataBaseManager

# Whats new

V0.0.8--maked dirctly executable for sqlite use shell by Executing 'python -m DataBaseManager -sqlite your_file_name'
fixed error in the shell
fixed bugs,
fixed error in installing on linux

# Versions

v0.0.1=>old stable Versions not stable
v0.0.2=>error in this version import prints a while loop
v0.0.3=>Stable version not recommended
v0.0.4=>fixed bugs. not supported multiprocess object. not recommended
v0.0.5=>new  object multiprocess for manageing multiple database at the same time. not supported directly executing shell. not recommended
v0.0.6=>new directly executing shell. 
v0.0.7=>new version . fixed error in installing on linux.
v0.0.8=>Fixed bugs