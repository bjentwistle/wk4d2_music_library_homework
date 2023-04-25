#This is basic code to speak to and connect to our database.

import psycopg2
import psycopg2.extras as ext


def run_sql(sql, values = None): #values would be used to INSERT new data into the db
    conn = None #connection is set to None
    results = [ ]
    try:
        conn = psycopg2.connect(dbname='music_library') #this connects us to the db we created notice quote marks, connect method of psycopg2 is expecting a str
        cur = conn.cursor(cursor_factory = ext.DictCursor) #the factory makes the cursor for us to step thru each row/dict of our data.
        cur.execute(sql, values) #this is like pressing enter on our keyboard
        conn.commit() #commit to running the code.
        results = cur.fetchall() #tells the cursor to grab all the rows (because we don't have a lot of rows but if there was a lot more we could use .fetchmany())
        cur.close() #close the cursor connection

    except (Exception, psycopg2.DatabaseError) as error:
        print("Becky you have an error message:", error)

    finally:
        if conn is not None: #checking the connection was make in the first place
            conn.close() #finally close the connection
    
    return results #return some results in python form