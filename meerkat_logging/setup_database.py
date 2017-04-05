#!/usr/bin/python3

"""
Database creation scripts for logging
"""
import sys, getopt
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

import model

def setup_database(url, base):
    try:
        if not database_exists(url):
            print('Creating database.')
            create_database(url)

    except exc.OperationalError as e:
        print('There was an error connecting to the db.')
        print(e)
        return False

    engine = create_engine(url)
    base.metadata.create_all(engine)

    return True



def parse_args(argv):
   database_url = ''
   try:
      opts, args = getopt.getopt(argv,"hd:",["database="])
   except getopt.GetoptError:
      print('Incorrect call, correct usage is setup_database.py -d <database_url>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('setup_database.py -d <database_url>')
         sys.exit()
      elif opt in ("-d", "--database"):
         database_url = arg
   print('Database URL is ', database_url)
   ret = setup_database(database_url, model.Base)
   if ret:
   	print("Database set up correctly")
   else:
   	print("Database set up failed")


if __name__ == "__main__":
   parse_args(sys.argv[1:])



