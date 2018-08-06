import argparse
import sqlite3
import sys
import os

COOKIE_TABLE = 'moz_cookies'
DOMAIN_COLUMN = 'baseDomain'
CONN_TEST_QUERY = 'SELECT * FROM ' + COOKIE_TABLE + ' LIMIT 1'

'''
Deletes the cookies from the database, with the
exception of any base domains that match the
given whitelist.
'''
def delete_cookies(database, whitelist) :

    sql_list = get_sql_list(whitelist)
    delete_query = 'DELETE FROM ' + COOKIE_TABLE + ' WHERE ' + DOMAIN_COLUMN + ' NOT IN ' + sql_list

    cursor = database.cursor()
    cursor.execute(delete_query)
    database.commit()

    print 'All specified cookies deleted.'

def get_sql_list(python_list) :

    if len(python_list) == 0 :
        return '()'

    sql_list = '('

    for item in python_list :
        sql_list = sql_list + '\'' + str(item) + '\'' + ', '

    sql_list = sql_list[:-2] + ')'

    return sql_list

def get_arguements() :

    arg_parser = argparse.ArgumentParser(description='Clears Firefox cookies.')
    arg_parser.add_argument('-d',
                            '--directory',
                            type=str,
                            help='The directory for your Firefox cookies. ' +
                                'This can be found by going to Firefox, then to ' +
                                'Help > Troubleshooting Information > Profile Directory.',
                            required=True)
    arg_parser.add_argument('-i',
                            '--ignore',
                            nargs='+',
                            type=str,
                            help='One or more domains which you do NOT want removed. ' +
                                'These must be the base domains (not subdomains). '
                                'Example: firefox_cookie_sweep.py --except aarondevelops.com google.com firefox.com')
                        
    return arg_parser.parse_args()

def validate_connection(database) :

    if is_valid_connection(database) == False :

        print 'An error occurred while connecting to the database located at ' + db_path
        print 'Please validate the location, or use --help for more details.' 
        
        database.close()
        sys.exit()

def is_valid_connection(database) :

    cursor = database.cursor()

    try :
        cursor.execute(CONN_TEST_QUERY)
    except sqlite3.OperationalError as e :
        print 'ERROR! ' + str(e)
        print "" # new line
        return False

if __name__ == "__main__" :
    
    args = get_arguements()

    db_path = os.path.join(args.directory, 'cookies.sqlite')
    whitelist = args.ignore if args.ignore else []

    database = sqlite3.connect(db_path)

    validate_connection(database)

    delete_cookies(database, whitelist)
    database.close()