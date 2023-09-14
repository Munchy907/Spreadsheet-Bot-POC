
BACKGROUND_COLOR_RED = 255
BACKGROUND_COLOR_GREEN = 124
BACKGROUND_COLOR_BLUE = 128
BACKGROUND_DIVIDER_VALUE = 255.0


def change_background_color(sheet_id, row_index, column_index):
    # print(row_index)
    # print(column_index)
    background_color_style = {
        'rgbColor': {  # To get uRGB for (0 - 1) rgb, divide by 255.0
            'red': BACKGROUND_COLOR_RED / BACKGROUND_DIVIDER_VALUE,
            'green': BACKGROUND_COLOR_GREEN / BACKGROUND_DIVIDER_VALUE,
            'blue': BACKGROUND_COLOR_BLUE / BACKGROUND_DIVIDER_VALUE,
        }
    }
    request = {
        'updateCells': {
            'rows': [
                {
                    'values': [
                        {
                            'userEnteredFormat': {
                                'backgroundColorStyle': background_color_style
                            }
                        }
                    ]
                }
            ],
            'fields': 'userEnteredFormat.backgroundColorStyle',
            'start': {
                "sheetId": sheet_id,
                "rowIndex": row_index,
                "columnIndex": column_index
            }
        }
    }
    return request
