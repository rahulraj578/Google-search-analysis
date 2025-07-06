pip install pytrends matplotlib panda seaborn plotly

#we use alias here so we don't have to write the whole name eveytime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from pytrends.request import TrendReq

# : This is a class from the pytrends library used to connect to Google Trends. It sets up a connection that allows you to query trend data.
# hl stands for host language and en-Us for english us 
pytrends = TrendReq(hl='en-US', tz= 360)
keyword= "cloud computing"

# cat means category here o represents all category
# geo='' means we need in global level
#  gprop means we only need google data not youtube or shopping data
pytrends.build_payload([keyword], cat=0, timeframe= 'today 12-m',geo='', gprop='')

region_data = pytrends.interest_by_region()

region_data = region_data.sort_values(by= keyword, ascending= False).head(15)
# ascending= false because we need in descending format

plt.figure(figsize = (10,6))
sns.barplot(x= region_data[keyword], y=region_data.index, palette= "Blues_d")
plt.title(f"Top Countries searching for '{keyword}'")
plt.xlabel("Interest")
plt.ylabel("Country")
plt.show()

region_data= region_data.reset_index()
# choropleth use for making world map
fig= px.choropleth(region_data,
                   locations='geoName',
                   locationmode= 'country names',
                   color= keyword,
                   title=f"Search Interest for'{keyword}' by Country",
                   color_continuous_scale = 'Blues')
fig.show()

time_df = pytrends.interest_over_time()

kw_list = ["cloud computing", "data science", " machine learning"]
pytrends.build_payload(kw_list, cat=0, timeframe= 'today 12-m', geo='', gprop='')

compare_df = pytrends.interest_over_time()
plt.figure(figsize=(12,6))
for kw in kw_list:
    plt.plot(compare_df.index, compare_df[kw], label= kw)

plt.title("keyword comparison over time")
plt.xlabel("Date")
plt.ylabel("Interest")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()




