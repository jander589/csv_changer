import pandas as pd

#read data from csv file
filename = 'SensorValues.csv'
df = pd.read_csv(
    filename,
    parse_dates=['Time']
)

rows = len(df.index) #number of rows in df
setRows = 6 #number of rows to be combined to one
iterations = int(rows/setRows) #number of iterations to be performed
print(iterations)

#combine set number of rows to one row
for x in range(iterations):
    df1 = df.iloc[setRows*x:setRows*(x+1),:]
    df1 = df1.max().to_frame().transpose()
    if(x==0):
        test = df1
    else:
        test = test.append(df1)
    print(x)

test = test.iloc[14717:132445] #Filter out bad readings
test = test[::10] #Slice every 10th value to only have 10min readings intervals
test.fillna(method='ffill', inplace=True) #Fill empty spaces with last valid observation

test.to_csv('new'+filename, index=False)