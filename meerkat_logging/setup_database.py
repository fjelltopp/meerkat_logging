#!/usr/bin/python3

"""
Database creation scripts for logging
"""
import sys, getopt
from sqlalchemy import create_engine, func, and_, exc, over, update, select, delete
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy.sql.expression import bindparam
from sqlalchemy_utils import database_exists, create_database, drop_database

from meerkat_logging import model

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
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('setup_database.py -d <database_url>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('setup_database.py -d <database_url>')
         sys.exit()
      elif opt in ("-d", "--database"):
         database_url = arg
   print('Database URL is ', database_url)
   setup_database(database_url, model.Base)


if __name__ == "__main__":
   parse_args(sys.argv[1:])



