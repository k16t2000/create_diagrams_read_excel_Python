import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas import DataFrame
import xlsxwriter
#diagramma kolon4ataja
# reading excel
f=pd.read_excel(r'C:\Users\37255\Desktop\algoritmi, python\grafiki\grafiki,4tenie iz faila\diagram.xlsx')
# print("Column headings:")
# print(f.columns)
# names=f['nimed']
# protsendid=f['Protsendid']
# print(f.nimed)
# print(f.Protsendid)


#print(f)#printing all datas from file with indexes

# a chart with 11 objects.
# print(f.head(11))#printing 11 rows from file
# f['Protsendid'].head(11).plot(kind="barh")#printing table with 11 rows
# plt.show()

pivot=f[['nimed','Protsendid']]
#print(pivot.head(len(pivot)))#if in head we do not mark quantity of rows, it is automaticaly shows 5 rows
n = pivot.pivot_table(index=['nimed'])
print(n.head(len(pivot)))#prints without indexes
n['Protsendid'].plot.barh(title='My first title, read from excel', colormap='jet')
plt.xlabel('Protsendid')
plt.ylabel('Nimed')
plt.axes().set_aspect(6)
plt.xlim((0,100))
plt.show()

#2 zadanie Elekter
file=pd.read_excel(r'C:\Users\37255\Desktop\algoritmi, python\grafiki\grafiki,4tenie iz faila\elekter.xlsx')
#print(file)#printing all datas from file with indexes
table=file[['Aasta','Hüdroenergia', 'Tuuleenergia', 'Puitkütus ja jäätmekütus']]
m = table.pivot_table(index=['Aasta'])
print(m.head(len(table)))#prints without indexes

m['Hüdroenergia'].plot.line(title='Elektrienergia tootmine taastuvatest allikatest, 2005-2018, excel', color='orange')
m['Tuuleenergia'].plot.line(color='olivedrab')
m['Puitkütus ja jäätmekütus'].plot.line(color='slategrey')

plt.xlabel('Aasta')
plt.ylabel('Gwh')
plt.legend() #add legend
#plt.axes().set_aspect(20)
#plt.xlim((0,100))
plt.show()

#3 zadanie Keskmine brutokuupalk, jaanuar 2007 – juuni 2019
f=pd.read_excel(r'C:\Users\37255\Desktop\algoritmi, python\grafiki\grafiki,4tenie iz faila\brutopalk.xlsx')
print(f)#print with indexes
tabel=f[['Year','January','February','March','April','May','June','July','August','September','October','November','December']]
bru = tabel.pivot_table(index=['Year'])
print(bru.head(len(tabel)))#prints without indexes

bru['January'].plot.barh(title='Average gross salary from January 2007- June 2019, excel', color='aqua')
bru['February'].plot.barh(color='orange')
bru['March'].plot.barh(color='darkred')
bru['April'].plot.barh(color='mediumpurple')
bru['May'].plot.barh(color='blue')
bru['June'].plot.barh(color='green')
bru['July'].plot.barh(color='pink')
bru['August'].plot.barh(color='yellow')
bru['September'].plot.barh(color='darkgoldenrod')
bru['October'].plot.barh(color='darkorange')
bru['November'].plot.barh(color='lavender')
bru['December'].plot.barh(color='navy')

plt.xlabel('Avg gross salary')
plt.ylabel('Year')
plt.legend() #add legend
plt.show()
