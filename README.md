# VK word searcher
This program designed to get statistic of appearance of 
specific word in public posts in [vk](https://vk.com) during 
specified period of time. The result of statistic data is
presented in bar chart using [chart-studio](https://chart-studio.plotly.com/feed/#/)
 service.

### How to Install

Python3 should be already installed. Then use pip (or pip3,
if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
To run API methods in this program you need to pass 
**access_token** - a special access key. You can get it 
by creating new  application in [vk](https://vk.com).

1. Create new application in [My Apps](https://vk.com/apps?act=manage) 
page for developers.
2. Application type should be *standalone*.
3. In your app settings please copy **Service token**, create
**.env** file and save there your Service token as 
```ACCESS_TOKEN = your Service token```.

Also you need to register at [chart-studio](https://chart-studio.plotly.com/feed/#/)
to get **username** and **API key**. Save them in **.env**
file as:
```
USER = "your user name"
API_KEY = "your API key"
```

### Project Goals
The code is written for educational purposes on online-course 
for web-developers [dvmn.org](https://dvmn.org).