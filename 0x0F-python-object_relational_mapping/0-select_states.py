#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    # Check the number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        c = db.cursor()

        # Execute the SQL query
        c.execute("SELECT * FROM `states`")

        # Print the results
        [print(state) for state in c.fetchall()]

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close the database connection
        if 'db' in locals() and db:
            db.close()
