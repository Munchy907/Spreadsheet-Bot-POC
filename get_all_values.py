def get_all_sheet_values(service, spreadsheet_id, sheet_range):
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id,
                                range=sheet_range).execute()
    values = result.get('values', [])

    if not values:
        print("No data found.")
    else:
        return values
