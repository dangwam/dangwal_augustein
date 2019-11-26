# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 13:52:21 2019

@author: MAYANK DANGWAL
"""

import mysql.connector

def my_db_func(id):
                    mydb = mysql.connector.connect(
                            host="localhost",
                            user="admin",
                            passwd="admin"
                            )
                    x1=int(id)
                    query="""select * from test_schema.breed where id=%i"""
                    mycursor = mydb.cursor()
                    #query =("select * from test_schema.breed where id=1")
                    mycursor.execute(query,x1)
                    myresult = mycursor.fetchall()
                    return myresult
     
#id=input("enter id::")
#x1=int(id)
#print(type(x1))
              
x=my_db_func(1)
print("Return Value is :: {}".format(x))