#############################################################################
#   Author: Nguyen Quoc Truong                                              #
#   Developer: T&T Stdudio                                                  #
#   Description: User, Google Sheet, Database can interact with each other. #
#                Send Mail, Write log after changing data.                  #
#   Usage:                                                                  #
#############################################################################

import os
import sys
from constants import DataMap as dm, Database as db, Managers as mng

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import pandas as pd
from sqlalchemy import create_engine
from unidecode import unidecode
from datetime import datetime
from SendMail import *


MODE_DATABASE = "db"
MODE_GGSHEET  = "sh"

data_dict = {
    'drink'    : [ dm.INVENTORY_SHEET, dm.DRINK_RANGE, dm.DRINK_COUNT_CELL, db.DRINK_TABLE ],
    'cake'     : [ dm.INVENTORY_SHEET, dm.CAKE_RANGE, dm.CAKE_COUNT_CELL, db.CAKE_TABLE ],
    'topping'  : [ dm.INVENTORY_SHEET, dm.TOPPING_RANGE, dm.TOPPING_COUNT_CELL, db.TOPPING_TABLE ],
    'material' : [ dm.INVENTORY_SHEET, dm.MATERIAL_RANGE, dm.MATERIAL_COUNT_CELL, db.MATERIAL_TABLE ],
    'bank'     : [ dm.GENERAL_INFO_SHEET, dm.BANK_INFO_RANGE, dm.BANK_INFO_COUNT_CELL, db.BANK_TABLE ],
    'info'     : [ dm.GENERAL_INFO_SHEET, dm.GENERAL_INFO_RANGE, db.INFO_TABLE ],
    'bill'     : [ dm.BILL_SHEET, dm.BILL_RANGE, dm.BILL_COUNT_CELL, db.BILL_TABLE ],
    'discount' : [],
    'history'  : [ dm.HISTORY_SHEET, dm.HISTORY_RANGE, dm.HISTORY_COUNT_CELL ]
}

class DataInterface:
    def __init__(self):
        self.credentials = None
        self.sheets = None
        self.__setup_access_datasheet()


    def __setup_access_datasheet(self):
        if os.path.exists(dm.GGS_TOKEN_PATH):
            self.credentials = Credentials.from_authorized_user_file(dm.GGS_TOKEN_PATH, dm.SCOPES)
        if not self.credentials or not self.credentials.valid:
            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                self.credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(dm.GGS_CREDENTIALS_PATH, dm.SCOPES)
                self.credentials = flow.run_local_server(port=0)
            with open(dm.GGS_TOKEN_PATH, "w") as token:
                token.write(self.credentials.to_json())
        if self.credentials is None:
            exit(1)
        else:
            try:
                service = build("sheets", "v4", credentials=self.credentials)
                self.sheets = service.spreadsheets()
            except HttpError as error:
                print(error)
                exit()


    def __get_cell_value(self, sheet_name, cell):
        cell_value = (self.sheets.values().get(
            spreadsheetId=dm.SPREADSHEET_ID,
            range=f"{sheet_name}!{cell}"
        ).execute().get("values")[0][0])
        return cell_value
    
    
    def __get_range_value(self, sheet_name, range):
        range_value = (self.sheets.values().get(
            spreadsheetId=dm.SPREADSHEET_ID,
            range=f"{sheet_name}!{range}"
        ).execute().get("values"))
        return range_value


    def __update_range_value(self, sheet_name, range, body_value):
        start_cell = str(range).split(":")[0]
        update_request = (self.sheets.values().update(
            spreadsheetId=dm.SPREADSHEET_ID,
            range=f"{sheet_name}!{start_cell}",
            body=body_value,
            valueInputOption="RAW"
        )).execute()
        return update_request
    
    
    def __clear_range_value(self, sheet_name, range): 
        clear_request = (self.sheets.values().clear(
            spreadsheetId=dm.SPREADSHEET_ID,
            range=f"{sheet_name}!{range}"
        )).execute()
        return clear_request
    

    # Fetch from Google Sheet to Database
    def fetch_table_data(self, data_name):
        if data_name not in data_dict:
            print(data_name + " is not exists in data map")    
            return None
        
        def convert_to_standard(series):
            return series.apply(lambda x: unidecode(x.lower()))
        
        if self.sheets is not None:
            data_list = data_dict[data_name]
            if len(data_list) < 4:
                range_value = self.__get_range_value(data_list[0], data_list[1])
            else:
                last_row = self.__get_cell_value(data_list[0], data_list[2])
                range_value = self.__get_range_value(data_list[0], data_list[1] % last_row)
            if range_value:
                df = pd.DataFrame(range_value[1:], columns=range_value[0])
                if data_name == 'drink':
                    df.insert(1, 'alias', convert_to_standard(df['drink']))
                return df, data_list[-1]
            else:
                print(f"No data found for {data_name}!")
                return None
        else:
            print("Can't reach to Data sheet")
            return None
    
    
    # Update from Database to Google Sheet
    def update_table_data(self, data_name, df):
        if data_name not in data_dict:
            print(data_name + " is not exists in data map")
            return None
        
        if self.sheets is not None:
            data_list = data_dict[data_name]
            # Clear before update            
            if len(data_list) < 4:
                clear_res = self.__clear_range_value(data_list[0], data_list[1])
            else:
                last_row = self.__get_cell_value(data_list[0], data_list[2])
                clear_res = self.__clear_range_value(data_list[0], data_list[1] % last_row)
                
            if clear_res:
                if data_name == "drink":
                    df = df.drop(columns="alias")
                values_to_update = [df.columns.values.tolist()] + df.values.tolist()
                value_range_body = { 'values': values_to_update }
                return self.__update_range_value(data_list[0], data_list[1], value_range_body)
            else:
                print("Clear failed!")
                return None
    
    
    # Write log modified when Updating/Fetching Database/Google Sheet
    def write_log_modified(self, time, mode, data_name, name, note):
        inventory = None
        if mode == MODE_GGSHEET:
            inventory = 'Google Sheet'
        else:
            inventory = 'Database'
        data_list = data_dict['history']
        list_data_str = ', '.join(data_name)
        row_number = int(self.__get_cell_value(data_list[0], data_list[2])) + 1
        values_to_update = [ [ time, list_data_str, inventory, name, note ] ]
        value_range_body = { 'values': values_to_update }
        return self.__update_range_value(data_list[0], data_list[1] % row_number, value_range_body)


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    engine = create_engine(db.DB_CONNECTION_STR % (username, password))
    
    if engine:
        di = DataInterface()
        if len(sys.argv) >= 6:
            mode = sys.argv[3]
            note = sys.argv[4]
            table_list = sys.argv[5:]
            try:
                run_result = None
                if mode == MODE_DATABASE:       # Update Database
                    print("Updating Database...")
                    for table in table_list:
                        df, table_name = di.fetch_table_data(table)
                        run_result = df.to_sql(table_name, con=engine, if_exists='replace', index=False)
                    print("Update Database successfully!")
                        
                elif mode == MODE_GGSHEET:      # Update GG sheet
                    print("Updating Google Sheet...")
                    for table in table_list:
                        query = f"SELECT * FROM {data_dict[table][-1]}"
                        df = pd.read_sql_query(query, engine)
                        run_result = di.update_table_data(table, df=df)
                    print("Update Google Sheet successfully!")
                        
                # Write log and Send mail
                if run_result is not None:
                    current_datetime = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")
                    di.write_log_modified(current_datetime, mode, table_list, get_manager_name(), note=note)
                    print("Log written")
                    send_email(create_message(get_manager_name(), current_datetime, table_list, mode, note))
                    print("Mail sent")
                else:
                    print("Failed to update data.")
            except Exception as e:
                print(f"An error occurred: {e}")
                    
        elif len(sys.argv) == 5:
            from_date = sys.argv[3] + ' 00:00:00'
            to_date = sys.argv[4] + ' 23:59:59'
            try:         
                query = f"SELECT date_time, items, discount_items FROM {data_dict['bill'][-1]} WHERE date_time >= '{from_date}' AND date_time <= '{to_date}'"
                df = pd.read_sql_query(query, engine)
                
                formatted_items = []
                for i in range(df['items'].count()):
                    row = str()
                    for item in df['items'][i]:
                        if item['id'] != "1":
                            row += "\n"
                        row += "{}) {}({}) - SL: {}".format(item['id'], item['name'], item['size'], item['quantity'])
                        if item['toppings']:
                            for tp in item['toppings']:
                                row += "\n\t+ {}".format(tp)
                    formatted_items.append(row)

                # Update the 'items' column in the DataFrame
                df['items'] = formatted_items
                df['date_time'] = df['date_time'].astype(str)
                di.update_table_data('bill', df)
            except Exception as e:
                print(f"An error occurred: {e}")

        else:
            print('Missing argurments')
            exit(1)
    else:
        print('Connection failed')
        exit(1)
