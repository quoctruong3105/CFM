#############################################################################
#   Author: Nguyen Quoc Truong                                              #
#   Developer: T&T Stdudio                                                  #
#   Description: Request credential to accesss Data Sheet when app set up.  #
#                Remove token file when app tear down.                      #
#   Usage: Included and used in DataInterface.py                            #
#############################################################################

import os
import sys
from google_auth_oauthlib.flow import InstalledAppFlow
from constants import DataMap as dm

def main(state):
    if state:        # App set up
        try:
            flow = InstalledAppFlow.from_client_secrets_file(dm.GGS_CREDENTIALS_PATH, dm.SCOPES)
            credentials = flow.run_local_server(port=0)
        except FileNotFoundError:
            print(f"File {dm.GGS_CREDENTIALS_PATH} not found.")
        with open(dm.GGS_TOKEN_PATH, "w") as token:
            token.write(credentials.to_json())
    else:            # App tear down
        try:
            os.remove(dm.GGS_TOKEN_PATH)
            print(f"File {dm.GGS_TOKEN_PATH} deleted successfully.")
        except FileNotFoundError:
            print(f"File {dm.GGS_TOKEN_PATH} not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <state>")
        sys.exit(1)
    try:
        state = eval(sys.argv[1].capitalize())
        main(state)
    except NameError:
        print("Invalid value for state. Please use 'True' or 'False'.")
        sys.exit(1)
