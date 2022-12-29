from tabulate import tabulate
def draw_table(table):
    print(tabulate(table, headers = ['User ID','Average Question','Participation Rate']))