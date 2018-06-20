
# coding: utf-8

# In[1]:


import requests


# In[2]:


response = requests.get('https://api.darksky.net/forecast/API/40.682944,-73.945972')
data = response.json()


# In[3]:


current = data['currently']
TEMPERATURE = current['temperature']


# In[4]:


SUMMARY = current['summary']


# In[5]:


daily = data['daily']
forecast = daily['data']
# forecast = forecast[0]
HIGH_TEMP = forecast[0]['temperatureHigh']


# In[6]:


LOW_TEMP = forecast[0]['temperatureLow']


# In[7]:


if HIGH_TEMP > 75:
    TEMP_FEELING = "hot"
elif HIGH_TEMP > 55:
    TEMP_FEELING = "comfortable"
elif HIGH_TEMP > 40:
    TEMP_FEELING = "cool"
else:
    TEMP_FEELING = "cold"


# In[8]:


if forecast[0]['precipProbability'] > .5:
    RAIN_WARNING = "Better take an umbrella!"
else:
    RAIN_WARNING = "You can probably leave the umbrella at home. Probably."


# In[9]:


todays_forecast = "Right now it is " + str(TEMPERATURE) + " degrees out and " + SUMMARY + ". Today will be " + TEMP_FEELING + " with a high of " + str(HIGH_TEMP) + " and a low of " + str(LOW_TEMP) + ". " + RAIN_WARNING


# In[10]:


import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%B %d, %Y")
subject_line = "Morning Forecast: " + date_string


# In[11]:


response = requests.post(
        "https://api.mailgun.net...",
        auth=("api", "API"),
        data={"from": "USER <DOMAIN.mailgun.org>",
              "to": ["email@gmail.com"],
              "subject": subject_line,
              "text": todays_forecast}) 
response.text

