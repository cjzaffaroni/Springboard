import sqlite3
from sqlite3 import Error


# Q1: Some of the facilities charge a fee to members, but some do not. Write a SQL query to produce a list of the names of the facilities that do.
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
 
    return conn

 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    
    query1 = """
        SELECT name
        FROM FACILITIES
        WHERE membercost = 0
        """

    cur.execute(query1)
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)


def main():
    database = "sqlite_db_pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn: 
        print("Question 01 & 02")
        select_all_tasks(conn)
 
 
if __name__ == '__main__':
    main()
#__________________________________________________________________________

# Q2: How many facilities do not charge a fee to members? ANSWER: 4

#__________________________________________________________________________


# Q3: Write an SQL query to show a list of facilities that charge a fee to members, where the fee is less than 20% of the facility's monthly maintenance cost. Return the facid, facility name, member cost, and monthly maintenance of the facilities in question. 

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
 
    return conn

 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    
    query1 = """
        SELECT facid, name, membercost, monthlymaintenance
        FROM FACILITIES
        WHERE membercost > 0 and membercost < (monthlymaintenance * 0.2);
        """

    cur.execute(query1)
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)


def main():
    database = "sqlite_db_pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn: 
        print("Question 03")
        select_all_tasks(conn)
 
 
if __name__ == '__main__':
    main()

#__________________________________________________________________________


# Q4: Write an SQL query to retrieve the details of facilities with ID 1 and 5. Try writing the query without using the OR operator. 

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
 
    return conn

 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    
    query1 = """
        SELECT *
        FROM FACILITIES
        WHERE facid IN (1,5);
        """

    cur.execute(query1)
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)


def main():
    database = "sqlite_db_pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn: 
        print("Question 04")
        select_all_tasks(conn)
 
 
if __name__ == '__main__':
    main()

#__________________________________________________________________________


# Q5: Produce a list of facilities, with each labelled as 'cheap' or 'expensive', depending on if their monthly maintenance cost is more than $100. Return the name and monthly maintenance of the facilities in question. 


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
 
    return conn

 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    
    query1 = """
        SELECT name, monthlymaintenance, case
	WHEN monthlymaintenance > 100 then 'expensive' else 'cheap' 
	end as cheap_expensive
        FROM FACILITIES;
        """

    cur.execute(query1)
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)


def main():
    database = "sqlite_db_pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn: 
        print("Question 05")
        select_all_tasks(conn)
 
 
if __name__ == '__main__':
    main()


#__________________________________________________________________________


# Q6: You'd like to get the first and last name of the last member(s) who signed up. Try not to use the LIMIT clause for your solution. 


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
 
    return conn

 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    
    query1 = """
        SELECT firstname, surname
        FROM MEMBERS
	WHERE joindate IN (
		SELECT MAX(joindate)
		FROM MEMBERS);
        """

    cur.execute(query1)
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)


def main():
    database = "sqlite_db_pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn: 
        print("Question 06")
        select_all_tasks(conn)
 
 
if __name__ == '__main__':
    main()


#__________________________________________________________________________


# Q7: Produce a list of all members who have used a tennis court. Include in your output the name of the court, and the name of the member formatted as a single column. Ensure no duplicate data, and order by the member name. 

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
 
    return conn

 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    
    query1 = """
	SELECT DISTINCT name||' '||firstname||' '||surname AS tennis_bookings
        FROM BOOKINGS
	LEFT JOIN FACILITIES USING(facid)
	LEFT JOIN MEMBERS USING (memid)
	WHERE facid IN (0,1) AND memid != 0 
	ORDER BY surname, name;
        """

    cur.execute(query1)
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)


def main():
    database = "sqlite_db_pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn: 
        print("Question 07")
        select_all_tasks(conn)
 
 
if __name__ == '__main__':
    main()


#__________________________________________________________________________


# Q8: Produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than 
# $30. Remember that guests have different costs to members (the listed costs are per half-hour 'slot')
# and the guest user's ID is always 0. Include in your output the name of the facility, the name of the
# member formatted as a single column, and the cost. Order by descending cost, and do not use any
# subqueries.

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
 
    return conn

 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    
    query1 = """
	SELECT name||' '||firstname||' '||surname AS Sep_14_bookings, case
	WHEN memid = 0 
		THEN slots * guestcost
		ELSE slots * membercost
		END AS cost
        FROM BOOKINGS
	LEFT JOIN FACILITIES USING(facid)
	LEFT JOIN MEMBERS USING(memid)
	WHERE starttime LIKE '2012-09-14%' AND cost > 30
	ORDER BY cost DESC;
        """

    cur.execute(query1)
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)


def main():
    database = "sqlite_db_pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn: 
        print("Question 08")
        select_all_tasks(conn)
 
 
if __name__ == '__main__':
    main()


#__________________________________________________________________________


# Q9:  This time, produce the same result as in Q8, but using a subquery.

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
 
    return conn

 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    
    query1 = """
	SELECT name||' '||firstname||' '||surname AS Sep_bookings, case
	WHEN memid = 0 
		THEN slots * guestcost
		ELSE slots * membercost
		END AS cost
        FROM (
		SELECT * 
		FROM BOOKINGS
		WHERE starttime LIKE '2012-09-14%')
	AS Sept_bookings 
	LEFT JOIN FACILITIES USING(facid)
	LEFT JOIN MEMBERS USING(memid)
	WHERE ( memid = 0 AND slots * guestcost > 30 )
	OR ( memid != 0 AND slots * membercost > 30 )
	ORDER BY cost DESC;
        """

    cur.execute(query1)
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)


def main():
    database = "sqlite_db_pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn: 
        print("Question 09")
        select_all_tasks(conn)
 
 
if __name__ == '__main__':
    main()


