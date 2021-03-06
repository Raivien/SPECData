# Author: Jasmine Oliveira
# Date: 06/27/2016
# SPECdata Configuration File:
#       * Specifies: Program Directory (path)
#                    Database Directory (path)
#                    Log Directory (path)



# Program directory
PROGRAM_DIR = ""
# Database directory
DATABASE_DIR = ""
# Log Directory
LOG_DIR = ""

##################################################################
####################### DO NOT EDIT BELOW ########################
##################################################################

# Imports
import sqlite3
import os

# GLOBAL CONFIG VARIABLES #
global db_path
global db_filepath
global conn

# SET VARIABLES TO DEFINED
db_dir = os.path.join(DATABASE_DIR , "data")
db_filepath = os.path.join(db_dir, "spectrum.db")
prog_dir = PROGRAM_DIR
conn = sqlite3.connect(db_filepath)