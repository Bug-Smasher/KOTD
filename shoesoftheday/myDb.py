import datetime
import sqlite3
import myShoes as shoedb


date_now = datetime.datetime.now()
myDb = sqlite3.connect("customer.db")
myCursor = myDb.cursor()

#myCursor.execute("""CREATE TABLE customer(
 #                   name text,
  #                  joinDate text,
   #                 age int
    #                )""")

#myCursor.execute("INSERT INTO customer VALUES ('John Doe', '01-12-2020', 27)")
#myCursor.execute("INSERT INTO customer VALUES (?,?,?)",(shoedb.name,date_now, shoedb.age))
myCursor.execute("SELECT * FROM customer WHERE name LIKE 'Lebron'")
print(myCursor.fetchone())
myDb.commit()




myDb.close()