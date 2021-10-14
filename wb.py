import pandas
wb = pandas.read_excel('mouser.xlsx')
print(wb['query'].iloc[0])
