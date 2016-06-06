#
# Database access functions for the web forum.
# 

import psycopg2
import time
# bleach to keep out spammy script
# sanitize data - using Bleach http://bleach.readthedocs.io/en/latest/
# import bleach


def GetAllPosts():
## Database connection
  DB = psycopg2.connect("dbname=forum")
  c = DB.cursor()
  c.execute("SELECT time, content FROM posts ORDER BY time DESC")
  posts = ({'content': str(row[1]), 'time': str(row[0])}
           for row in c.fetchall())
  DB.close()
  return posts


## Add a post to the database.
def AddPost(content):
  DB = psycopg2.connect("dbname=forum")
  c = DB.cursor()
# Clean content before inserting into the database  
#  content = bleach.clean(content)

# Insert into the database what we put in the webpage.
  c.execute("INSERT INTO posts (content) VALUES ('%s')" % content)

  # (content,)) is a tuple parameter because of the comma the string is now just read as only text.
  # You must use %d for integer values and %s for string values.
#  c.execute("INSERT INTO posts (content) VALUES (%s)", (content,))


  ################################################################################
  #c.execute("UPDATE posts SET content = 'cheese' WHERE content LIKE '%spam%';")
  #c.execute("DELETE FROM posts WHERE content LIKE 'cheese';")
  DB.commit()
  DB.close()

# 2. sql injection attack-bobby tables.
# '); delete from posts; --  
# The database will treat this as a database command




# Copy and add this to the forum post. The webserver will think this is should be executed.
# Script injection attack
''' <script>
setTimeout(function() {
    var tt = document.getElementById('content');
    tt.value = "<h2 style='color: #FF6699; font-family: Comic Sans MS'>HACKED, HACKED, HACKED, HACKED,<br>YOU GOT HACKED!</h2>";
    tt.form.submit();
}, 2500);
</script>'''

