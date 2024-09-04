import mysql.connector

# Initialize a variable to hold the database connection
conn = None

try:
    # Attempt to establish a connection to the MySQL database
    conn = mysql.connector.connect(host='localhost', 
                                   port=3306,
                                   database='pub',
                                   user='<user>',
                                   password='<password>')
    
    # Check if the connection is successfully established
    if conn.is_connected():
        print('Connected to MySQL database')

except mysql.connector.Error as e:
    # Print an error message if a connection error occurs
    print(e)

finally:
    # Close the database connection in the 'finally' block to ensure it happens
    if conn is not None and conn.is_connected():
        conn.close()

# 첫번째

import mysql.connector

# Initialize a variable to hold the database connection
conn = None

try:
    # Attempt to establish a connection to the MySQL database
    conn = mysql.connector.connect(host='localhost', 
                                   port=3306,
                                   database='pub',
                                   user='<user>',
                                   password='<password>')
    
    # Check if the connection is successfully established
    if conn.is_connected():
        print('Connected to MySQL database')

except mysql.connector.Error as e:
    # Print an error message if a connection error occurs
    print(e)

finally:
    # Close the database connection in the 'finally' block to ensure it happens
    if conn is not None and conn.is_connected():
        conn.close()

# 두번째

[mysql]
host = localhost
port = 3306
database = pub
user = <user>
password = <password>

# 첫번째

[mysql]
host = localhost
port = 3306
database = pub
user = <user>
password = <password>

# 두번째

from configparser import ConfigParser

def read_config(filename='app.ini', section='mysql'):    
    # Create a ConfigParser object to handle INI file parsing
    config = ConfigParser()
    
    # Read the specified INI configuration file
    config.read(filename)

    # Initialize an empty dictionary to store configuration data
    data = {}

    # Check if the specified section exists in the INI file
    if config.has_section(section):
        # Retrieve all key-value pairs within the specified section
        items = config.items(section)

        # Populate the data dictionary with the key-value pairs
        for item in items:
            data[item[0]] = item[1]
    else:
        # Raise an exception if the specified section is not found
        raise Exception(f'{section} section not found in the {filename} file')

    # Return the populated data dictionary
    return data

if __name__ == '__main__':
    # Read the configuration from the default section ('mysql') in the 'app.ini' file
    config = read_config()

    # Display the obtained configuration
    print(config)

# 첫번째
