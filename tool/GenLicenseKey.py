#############################################################################
#   Author: Nguyen Quoc Truong                                              #
#   Developer: T&T Stdudio                                                  #
#   Description: Generate license key for managers devices and pos devices. #
#                The key is used on both CFM and CFSW software.             #
#   Usage: python GenLicenseKey.py "mac_id" "hostname"                      #
#############################################################################

import sys
import hashlib
import base64
import psycopg2
from psycopg2 import sql
import re
from constants import Product as pd, Database as db
from GetMachineInfo import *

def generate_license_key(product_name, mac_id, machine_product_id):
    # Combine product key and hardware ID
    combined_data = f"{product_name}:{mac_id}:{machine_product_id}"
    # Hash the combined data
    hashed_data = hashlib.sha256(combined_data.encode()).digest()
    # Base64 encode the hashed data
    license_key = base64.b64encode(hashed_data).decode()
    return license_key

    
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    #mid = sys.argv[3] 
    #mpi = sys.argv[4]
    mid = get_mac_address() 
    mpi = get_machine_product_id()
    
    pattern = re.compile(r"postgresql://([^:]+):([^@]+)@([^:/]+):([^/]+)/(.+)")
    match = pattern.match(db.DB_CONNECTION_STR % (username, password))

    conn = psycopg2.connect(
        dbname=match.group(5),
        user=match.group(1),
        password=match.group(2),
        host=match.group(3),
        port=match.group(4)
    )
    
    # Create a cursor object to execute SQL queries
    if conn is not None:
        cursor = conn.cursor()

        # Query the database
        select_query = "SELECT * FROM license_keys"
        cursor.execute(select_query)
        keys = cursor.fetchall()

        # Print the results
        my_key = generate_license_key(pd.NAME, mac_id=mid, machine_product_id=mpi)
        
        for key in keys:
            if key[0] == my_key:
                print("Key exists already")
                exit()
        
        # Insert data into the table
        insert_data_query = "INSERT INTO license_keys (key) VALUES (%s)"
        data_to_insert = (str(my_key),)
        cursor.execute(insert_data_query, data_to_insert)

        # Commit the changes
        conn.commit()

        # Close the cursor and the connection
        cursor.close()
        conn.close()
        
    else:
        print("Connection failed")
        exit(1)
    
