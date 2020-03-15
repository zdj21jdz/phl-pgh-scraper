#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:36:02 2020

@author - Zach Jansma

Python news feed scraper for Pittsburgh News, weather, and sports!
- News feed from WTAE
- Weather from openweather API
-TODO - Sports from ESPN
 
Date written - 03/15/2020
Last Update - 03/15/2020
"""
# Import libraries
import feedparser as fp # Used to parse xml feed from WTAE
import requests as r # Used for HTTP requests
import os # Used to check environment variables for open weather
import re # Used to clean html tags from WTAE's news article descriptions

# Pittsburgh News from WTAE
class PittNews:
    
    # Initialize class by grabbing articles from the site
    def __init__(self):
        # Create object to grab the xml from rss feed
        NewsFeed = fp.parse("https://www.wtae.com/topstories-rss")
        
        # Grab all articles from xml
        self.articles = NewsFeed.entries
    
    # Remove html tags from news description
    def htmlTagRemoval(self, text):
        # Set regex to remove tags
        tag_remover = re.compile(r'<[^>]+>')
        
        # Return cleaned text
        return tag_remover.sub('',text)
    
    # Print out a specific number of articles to the prompt
    def getArticles(self, num_articles):
        # Blank string to catch all the artiles
        news = ""
        
        # Loop through the number of articles the user wishes to see
        for x in range(int(num_articles)):
            # Grab title
            news += self.articles[x].title + "\n"
            
            # Grab publication date
            news += "Publication Date: " + self.articles[x].published + "\n"
            
            # Break to nicely separate title from summary
            news += "----------------------------------------------\n"
            
            # Summary of the Article - clean out html tags
            news += self.htmlTagRemoval(self.articles[x].description) + "\n"
            
            # Link to Article
            news += "Link to article: " + self.articles[x].link + "\n"
            
            # New lines to separate next news story
            news += "\n"
            
        return news
    
class PittWeather:
    
    # Initialize class
    def __init__(self):
        # Check to ensure API key is set up in environment variables
        if "OPEN_WEATHER_API_KEY" not in os.environ:
            raise EnvironmentError('Open Weather API not stored in environment variables')
            exit(1)
            
        # Get API Key
        self.appid = os.environ['OPEN_WEATHER_API_KEY']
        
        # Set city and country
        self.city = 'Pittsburgh,US'
        
        # Base URL
        self.url = ('https://api.openweathermap.org/data/2.5/weather'
                    + '?q=' + self.city
                    + '&units=imperial' # So we can get temp in F
                    + '&APPID=' + self.appid)
            # Call Api to get weather from a City
    def getPittWeather(self):
        # Get request for weather App
        weather = r.get(self.url)
        
        # Convert output to JSON
        weather = weather.json()
        
        # Blank string to catch all the info from weather
        output = "\nPittsburgh Weather:\n"
        
        # Add Weather Description
        output += ("Today, you can expect - " 
                   + weather['weather'][0]['description'] 
                   + '\n')
        
        # Add current temp
        output += ('Current Temp: ' 
                   + str(weather['main']['temp']) 
                   + 'F\n')
        
        # Add max and min temp
        output += ('Max Temp: ' 
                   + str(weather['main']['temp_max']) 
                   + 'F\n'
                   + 'Min Temp: ' 
                   + str(weather['main']['temp_min'])
                   + 'F\n')
        
        return output
