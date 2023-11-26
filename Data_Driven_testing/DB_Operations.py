#### insert,update,delete
'''insert_query = "insert into hello values(5,'Mr','Behera')"
update_query = "update hello set fname='Mrs' where slno=1"
delete_query = "delete from hello where slno=4"
import mysql.connector
try:
    con = mysql.connector.connect(host="localhost",port=3306,user="root",password="Bikash1998",database="mydb")
    curs = con.cursor()          #create cursor
    curs.execute(update_query)           #execute query through cursor
    con.commit()                 # commit transaction
    con.close()
except:
    print("Connection Failed.....")

print("finished......")'''

### select
import mysql.connector
try:
    con = mysql.connector.connect(host="localhost",port=3306,user="root",password="Bikash1998",database="mydb")
    curs = con.cursor()          #create cursor
    curs.execute("select * from hello")

    for row in curs:
        print(row[0],row[1],row[2])

    con.close()
except:
    print("Connection Failed.....")

print("finished......")
