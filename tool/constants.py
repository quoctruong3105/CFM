import os
from datetime import date

class Product:
    NAME = "CFSW-v1.0"
    PATH = os.path.dirname(os.getcwd())

class Managers:
    MANAGER_LIST = {
        'truong': [ 'Trường', 'quoctruong3105@gmail.com' ],
        'hieu'  : [ 'Hiếu', 'hieudv.job@gmail.com', 'macid' ],
        'khoi'  : [ 'Khôi', 'minhkhoiofficial0o0@gmail.com' ]
    }
    
    BOT_GMAIL          = 'hicfbot@gmail.com'
    BOT_GMAIL_APP_PASS = 'idav bbbx jget vnyc'
    MAIL_SUBJECT       = "HICF BOT - BÁO CÁO CẬP NHẬT"

class DataMap:
    SCOPES               = ["https://www.googleapis.com/auth/spreadsheets"]
    SPREADSHEET_ID       = '1JwDXk6rBjz5NCa-uyOG49sTDQt0R27Vke3UR0uje7Sg'
    # Use on local
    GGS_CREDENTIALS_PATH = 'E:/CFM/docs/ggsheet_creds.json'
    GGS_TOKEN_PATH       = 'E:/CFM/docs/token.json'
    # Use when release
    # GGS_CREDENTIALS_PATH = os.path.join(Product.PATH + "\\docs\\credentials.json")
    # GGS_TOKEN_PATH       = os.path.join(Product.PATH + "\\docs\\token.json")

    # constants for inventory sheet
    INVENTORY_SHEET      = 'inventory'
    # drink
    DRINK_RANGE          = 'A2:G%s'
    DRINK_COUNT_CELL     = 'G1'
    # material
    MATERIAL_RANGE       = 'I2:L%s'
    MATERIAL_COUNT_CELL  = 'L1'
    # cake
    CAKE_RANGE           = 'N2:P%s'
    CAKE_COUNT_CELL      = 'P1'
    # topping
    TOPPING_RANGE        = 'R2:V%s'
    TOPPING_COUNT_CELL   = 'V1'
    
    # constants for general info
    GENERAL_INFO_SHEET   = 'info'
    # general information
    GENERAL_INFO_RANGE   = 'B2:B6'
    # bank information
    BANK_INFO_RANGE      = 'D2:F%s'
    BANK_INFO_COUNT_CELL = 'F1'
    
    # constants for bill
    BILL_SHEET           = 'bill'
    BILL_RANGE           = 'A2:I%s'
    BILL_COUNT_CELL      = 'C1'
    
    # constants for modified history
    HISTORY_SHEET        = 'modified_history'
    HISTORY_COUNT_CELL   = 'E1'
    HISTORY_RANGE        = 'A%s:Ex'
    
class Database:
    DB_CONNECTION_STR  = 'postgresql://%s:%s@localhost:5432/cf_prj_test'
    DRINK_TABLE        = 'drinks'
    CAKE_TABLE         = 'cakes'
    MATERIAL_TABLE     = 'materials'
    TOPPING_TABLE      = 'toppings'
    INFO_TABLE         = 'constvalues'
    BANK_TABLE         = 'banks'
    BILL_TABLE         = 'bills'
    