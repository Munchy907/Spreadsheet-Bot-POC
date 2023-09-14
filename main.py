from __future__ import print_function

import os.path
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from background_color_changer import change_background_color
from get_all_values import get_all_sheet_values
from oAuth import authenticate

SPREADSHEET_ID = '1qSxNCeUAZ3TXO-IbdJaacGBJvGhgvIbxTqYeM8e8B1g'
SHEET_ID = 1434803629
RANGE_NAME = 'Tiers!A2:M'
# ROW_INDEX = 16
# COLUMN_INDEX = 3
SHEET_NAMES = ["Tierlist", "Tiers"]
SPREADSHEET_ARRAY = []


def main(highlight_item):
    creds = authenticate()
    try:
        service = build('sheets', 'v4', credentials=creds)
        values = get_all_sheet_values(service, SPREADSHEET_ID, RANGE_NAME)
        row_count = 0
        for row in values:
            row_count += 1
            column_count = -1
            for column in row:
                column_count += 1
                if column == highlight_item:
                    request = change_background_color(SHEET_ID, row_count, column_count)
                    response = service.spreadsheets().batchUpdate(
                        spreadsheetId=SPREADSHEET_ID,
                        body={'requests': [request]}
                    ).execute()
                    return True
        return False

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    if main(str(sys.argv[1])):
        print("Item updated")
    else:
        print("Item not found")

