import openpyxl
# for more documentation continue reading at http://python-simple.com/python-autres-modules-non-standards/openpyxl.php
# the directory for more info is at https://1drv.ms/u/s!Ak5XyBWR45TUsaRjH3MLEMBvH03ofQ?e=x311PM

# document = xlrd.open_workbook("ressources_divers/Modele-FAQ-Vizir.xlsx")
workbook = openpyxl.load_workbook('ressources_divers/Modele-FAQ-Vizir.xlsx')
print(workbook.sheetnames)
print(workbook['FAQ Teams']['A1'].value)
