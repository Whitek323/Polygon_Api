#pip install polygon
#pip install polygon-api-client
#pip install plotly
#pip install pandas
from polygon import RESTClient 
import config
import json

from typing import cast
from urllib3 import HTTPResponse

from plotly import graph_objects as go
import pandas as pd
import talib
client = RESTClient(config.API_KEY)

aggs = cast(
    HTTPResponse,
    client.get_aggs(
        'AAPL',
        1,
        'day',
        '2022-05-20',
        '2022-11-11',
        raw=True
    )
)
closeList = []
openList = []
highList = []
lowList = []
timeList = []
data = json.loads(aggs.data)
for item in data:
    if item == 'results':
        rawData = data[item]
for bar in rawData:
    for categoy in bar:
        if categoy == 'c':
            closeList.append(bar[categoy])
        elif categoy == 'h':
            highList.append(bar[categoy])
        elif categoy == 'l':
            lowList.append(bar[categoy])
        elif categoy == 'o':
            openList.append(bar[categoy])
        elif categoy == 't':
            timeList.append(bar[categoy])
times = []
for time in timeList:
    times.append(pd.Timestamp(time,tz='GMT',unit='ms'))
fig = go.Figure()
fig.add_trace(go.Candlestick(x=times,open=openList,high=highList,low=lowList,close = closeList,name='Apple Marget Data'))
fig.update_layout(xaxis_rangeslider_visible=False,template='plotly_dark')
fig.show()