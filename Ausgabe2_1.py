import csv
import numpy as np
f = open('master_data.csv', newline='')
g = open('sales_data.csv',newline = '')
master_data_reader = csv.reader(f, delimiter=',')
sales_data_reader = csv.reader(g, delimiter=',')
list = []
list2 = []
manager = []
country = []
sales_manager = []
sales_country = []
output_country = []
for elem in master_data_reader:
    list.append(elem)
for elem in sales_data_reader:
    list2.append(elem)

for i in range(0,6):
    manager.append(list[i][0])
    country.append(list[i][1])
for i in country:
    print(i)
    if i not in output_country:
        output_country.append(i)
output_country.remove('Country')
len_o_u = len(output_country)

print(len_o_u)
print(output_country)
list3 = []
sales_value = []
len1=int(len(list))
len2 = int(len(list2))
for i in range(0,len2):
    sales_manager.append(list2[i][0])
    sales_country.append(list2[i][1])
    sales_value.append(list2[i][2])
    for j in range(0,len1):
        if list2[i][0] == list[j][0]:
            list3.append(list[j][1])
print(len1, len2)
np.array(sales_value)
np.array(list3)
Us = 0
Fr=0
print(list3)
for i in range(0,(len2-1)):
    if list3[i] == 'United States':
        Us =Us + int(sales_value[i+1])
    else:
        Fr = Fr + int(sales_value[i+1])
print (Us, Fr)