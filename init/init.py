# Author: Jasmine Oliveira
# Date: 06/27/2016

import sqlite3
import os, sys
from config import *

# Create 'data' directory
if not os.path.exists(db_dir):
    os.makedirs(db_dir)

print "[Created Directory: " + db_dir + "]"

# Create spectrum database file
conn = sqlite3.connect(db_filepath)
print "[Created Database File: " + db_filepath + " ]"

# Create Cursor
cursor = conn.cursor()

# Execute SQL Script 'build_tables'
script = open('./build_tables', 'r').read()
sqlite3.complete_statement(script)

try:
    cursor.executescript(script)
except Exception as e:
    cursor.close()
    raise
print "[Built Tables]"

# Close DB connection
conn.close()
print "[INIT COMPLETE]"