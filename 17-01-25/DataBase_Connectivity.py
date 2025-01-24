import mysql.connector as c


mydb = c.connect(
    host="localhost",
    user="root",
    password="system",
    database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("create table teachers(tid int,tname varchar(20),dept varchar(20))")
id=input("Enter your id:")
name = input("Enter your name: ")
dept=input("Enter department")

mycursor.execute("insert into teachers values(%s,%s,%s)",(id,name,dept))
print("Records insrted succesfully")
mycursor.execute("update teachers set dept=%s,tname=%s where tid=%s",(dept,name,id))
mycursor.execute("delete from teachers where tid=%s",(id,))
mycursor.execute("select *from teachers")
mycursor.execute("select *from teachers group by tname order by tname asc")
mycursor.execute("select *from teachers where dept='it'")
mycursor.execute("select *from teachers where tid between 0 and 2")
teacher=mycursor.fetchall()
for i in teacher:
    print(i)

mydb.commit()