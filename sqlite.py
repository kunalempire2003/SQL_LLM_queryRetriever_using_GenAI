import sqlite3

connection=sqlite3.connect("STUDENTS.db")
cursor=connection.cursor()

table_info="""
   Create table STUDENTS(NAME VARCHAR(20),CLASS VARCHAR(20),
   SECTION VARCHAR(20),MARKS INT);



"""
cursor.execute(table_info)

cursor.execute('''Insert into STUDENTS values('Kunal','computer engineering','A',40)''')
cursor.execute('''Insert into STUDENTS values('Ram','IT','B',18)''')
cursor.execute('''Insert into STUDENTS values('Lalit','DataScience','A',29)''')
cursor.execute('''Insert into STUDENTS values('Kartik','computer engineering','A',24)''')
cursor.execute('''Insert into STUDENTS values('Jiten','computer engineering','B',35)''')
cursor.execute('''Insert into STUDENTS values('Ayush','Devops','C',32)''')
cursor.execute('''Insert into STUDENTS values('Bharat','IT','B',20)''')


#DISPLAY
print("The inserted records are")
data=cursor.execute('''Select*from STUDENTS''')
for row in data:
    print(row)


connection.commit()
connection.close()    