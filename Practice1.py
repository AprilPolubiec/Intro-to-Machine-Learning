import pandas as pd
import matplotlib.pyplot as plt

#1. Create function to output headers
def header(text):
    print('*****',text,'*****')

#2. Open/read data
data = pd.read_csv('./Pandas Tutorial/weather.txt')

weather_df = pd.DataFrame(data)

#3. Print dataframe
header('All weather data')
print(weather_df)

#4. Print descriptives for weather dataframe
header('Weather descriptives')
print(weather_df.describe())
print('Number of rows:', weather_df.shape[0], 'Number of columns:', weather_df.shape[1])

#5. Get descriptives for each season
#Method 1: indexing/creating new DFs
summer = weather_df.iloc[5:8]
fall = weather_df.iloc[8:11]
winter = pd.concat([weather_df.iloc[11:12],weather_df.iloc[0:2]])
spring = weather_df.loc['2':'4']

header('Summer Descriptives')
print(summer.describe())
header('Fall Descriptives')
print(fall.describe())
header('Winter Descriptives')
print(winter.describe())
header('Spring Descriptives')
print(spring.describe())

#Method 2: Groupby/apply
def findSeason(month):
    if (month == 'Jan') or (month == 'Feb') or (month == 'Dec'):
        return 'winter'
    elif (month == 'Mar') or (month == 'Apr') or (month == 'May'):
        return 'spring'
    elif (month == 'Jun') or (month == 'Jul') or (month == 'Aug'):
        return 'summer'
    elif (month == 'Sep') or (month == 'Oct') or (month == 'Nov'):
        return 'fall'

weather_df['season'] = weather_df.month
weather_df['season'] = weather_df.season.apply(
    lambda x:
    findSeason(x)
)

header('Summer Descriptives')
print(weather_df.groupby('season').describe().loc['summer'])
header('Fall Descriptives')
print(weather_df.groupby('season').describe().loc['fall'])
header('Winter Descriptives')
print(weather_df.groupby('season').describe().loc['winter'])
header('Spring Descriptives')
print(weather_df.groupby('season').describe().loc['spring'])

#6. Pull a random sample from the data frame
header('Random sample from weather table')
sample = weather_df.sample(n=5, replace=False)
print(sample)


########DATA VISUALIZATION
#7. Make scatterplot of month(index value) & record high
import matplotlib.pyplot as plt
plt.plot(weather_df.iloc[:,0], weather_df.record_high)

