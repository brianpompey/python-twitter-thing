import gspread

gc = gspread.service_account('credentials.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open("tester-spreadsheet").sheet1

# Update a range of cells using the top left corner address
wks.update('A1', [[2, 3], [4, 5]])

# Or update a single cell
wks.update('B42', "it's down there somewhere, let me take a look.")

# Format the header
wks.format('A1:B1', {'textFormat': {'bold': True}}) 