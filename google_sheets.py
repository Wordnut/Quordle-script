from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pandas as pd
import os
from datetime import datetime


def sheet_append(answers, game):
    # The key of the spreadsheet we want to access
    spreadsheet_key = "1wzYueKG4xeLnvC2WpmwCgH4MTJEWe_olAfKuFoqwVUE"

    ## Connect to our service account
    scope = ["https://spreadsheets.google.com/feeds"]
    # Use the service account credentials to authorize our application (have also attached this credentials file)
    config_path = os.path.join(os.path.dirname(__file__), "./google-credentials.json")
    credentials = ServiceAccountCredentials.from_json_keyfile_name(config_path, scope)
    gc = gspread.authorize(credentials)
    book = gc.open_by_key(spreadsheet_key)

    try:
        worksheet = book.worksheet(game)
    except Exception as e:
        print(
            f"[{__name__}]-[{datetime.now().strftime('%D %H:%M:%S')}] - Error in reading Sheet: {e}"
        )
    else:
        gs = gc.open_by_key(spreadsheet_key)

        # Append the data to the specified sheet within the spreadsheet
        data_values = [datetime.now().strftime('%Y-%m-%d')]
        
        data_values.extend(answers)

        gs.values_append(game, {"valueInputOption": "RAW"}, {"values": [data_values]})