from openpyxl import load_workbook
from openpyxl.styles import Font
from openpyxl.styles import Border


def toRemoveBold(file_destination):
    # To Remove bold, there is no existing way,
    # We have to use openpyxl, load the workbook,
    # then get worksheet and then update the cells of row one-by-one and then save

    workbook = load_workbook(file_destination)
    workSheet = workbook.get_sheet_by_name('Sheet1')
    for cell in workSheet["1:1"]:
        cell.font = Font(bold=False)
        cell.border = Border(top=None)
    workbook.save(file_destination)