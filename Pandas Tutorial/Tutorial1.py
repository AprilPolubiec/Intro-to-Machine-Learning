#Following tutorial found at https://youtu.be/e60ItwlZTKM

import numpy as np
import pandas as pd

def header(msg):
    print('-' * 50)
    print('[ ' + msg + ' ]')


header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],    #assigns index for each row
	columns = ['month','avg_high','avg_low','record_high',
                   'record_low','avg_precipitation']) #assigns names for each column
print(df)
 
header("2. read text file into a dataframe")
filename = "weather.txt"
df = pd.read_csv(filename)
print(df)

header("3. print first 5 or last 3 rows of df")
header("first 5 rows of df")
print(df.head()) #gives first 5 as default
header("last 3 rows of df")
print(df.tail()) #gives last 5 as default

header("4. get data types, index, columns, values")
header("data types")
print(df.dtypes)

header("index")
print(df.index)

header("columns")
print(df.columns)

header("values") #not used often
print(df.values)

header("5. Getting descriptive stats")
print(df.describe())

header("6. Sorting df")
print(df.sort_values('record_high', ascending=False))


header("7. Slicing DFs")
header("df.avg_low")    #single column
print(df.avg_low)

header("df['avg_low']")
print(df['avg_low'])        #single column

header("df[2:4]")
print(df[2:4])          #rows 2-4

header("df[['avg_low', 'avg_high']]")
print(df[['avg_low', 'avg_high']]) #passing a list to the [] (that's why [[]])

header("df.loc[:,['avg_low', 'avg_high']]")
print(df.loc[:,['avg_low', 'avg_high']]) #df.loc[from_row:to_row,['column1','column2']]

header("scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("df.iloc[3:5,[0:3]]")
print(df.iloc[3:5,[0,3]])   #rows 3-5 and columns 0-3





