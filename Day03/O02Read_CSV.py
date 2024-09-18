
import csv
from prettytable import PrettyTable

with open("Employee.csv", "r") as CSVR:
    emp_details = csv.reader(CSVR)
    # colNames = next(emp_details)
    # print(*colNames)

    emp_table = PrettyTable(next(emp_details))

    for row in emp_details:
        # print(*row)
        emp_table.add_row(row)

print(emp_table)
