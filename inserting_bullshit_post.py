# blog posts is a table (Title , Post)

import sqlite3 as db

connection = db.connect('Blog.db')
cursor = connection.cursor()

#creating the blog table
#cursor.execute("""CREATE TABLE posts(title TEXT,post TEXT)""")

##Inserting test data (random garbage)
blog_entry= [('Test Post 1',"This is really Awesome"),("Hello Everyone","I love Uofa. Studying here is Awesome"),("Post 3","Let me warn you... This is rubbish")]
cursor.executemany("INSERT INTO posts VALUES(?,?)",blog_entry)
connection.commit()
connection.close()


