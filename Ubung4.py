import csv
import numpy as np
f = open('master_data.csv', newline='')
g = open('sales_data.csv',newline = '')
master_data_reader = csv.reader(f, delimiter=',')
sales_data_reader = csv.reader(g, delimiter=',')
masterdata = []
salesdata = []
country = []
sales_country = []
output_country = []
for elem in master_data_reader:
    masterdata.append(elem)
for elem in sales_data_reader:
    salesdata.append(elem)
Len_Master=int(len(masterdata))
Len_Sales = int(len(salesdata))

for i in range(0,Len_Master):
    country.append(masterdata[i][1])
for i in country:
    print(i)
    if i not in output_country:
        output_country.append(i)
output_country.remove('Country')
len_o_u = len(output_country)

print(len_o_u)
print(output_country)
Sales_each_country = []
sales_value = []

for i in range(0,Len_Sales):

    sales_value.append(salesdata[i][2])
    for j in range(0,Len_Master):
        if salesdata[i][0] == masterdata[j][0]:
            Sales_each_country.append(masterdata[j][1])
print(Len_Master, Len_Sales)
np.array(sales_value)
np.array(Sales_each_country)
Sales = np.zeros(len_o_u)
print(Sales_each_country)
for i in range(0,(Len_Sales-1)):
    for j in range(0,len_o_u):
        if Sales_each_country[i] == output_country[j]:
            Sales[j] =Sales[j] + int(sales_value[i+1])

for i in range(0,len_o_u):
    print(output_country[i],Sales[i])