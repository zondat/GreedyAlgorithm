import openpyxl

# Search object by name
def search(objects, name):
    for i in range(0, len(objects)):
        if objects[i].name == name:
            found_object = objects[i]
            return found_object
    return None
    
def read_data(file_path):
    # Open the Excel file
    workbook = open_workbook(file_path)

    # Select the desired worksheet
    sheet_name = 'Sheet1'
    worksheet = open_sheet(workbook, sheet_name)  # Replace 'Sheet1' with the actual sheet name

    # Read the value of a specific cell
    cell_value = get_cell_data(worksheet, 'A', 1)  # Replace 'A1' with the desired cell reference

    # Print the cell value
    print(cell_value)

def open_workbook(file_path):
    return openpyxl.load_workbook(file_path)
    
def open_sheet(workbook, sheet_name):
    return workbook[sheet_name]
    
def get_cell_data(worksheet, row, col):
    cell_label = col + str(row)
    return worksheet[cell_label].value

#read_data('data.xlsx')