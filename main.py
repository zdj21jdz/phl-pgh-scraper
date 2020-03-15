#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 16:03:46 2020

@author: zach

Main program to show how classes work

Date written - 03/15/2020
Last Update - 03/15/2020
"""
# Import all libraries
import PittScraper
import PhillyScraper

### -- -- Initialize all objects -- -- ###
# News Scrapers
PhillyNews = PhillyScraper.PhillyNews()
PittNews = PittScraper.PittNews()

# Weather Info
PittWeather = PittScraper.PittWeather()
PhillyWeather = PhillyScraper.itsAlwaysSunny()

# Sports info -- TODO

if __name__ == '__main__':
    ### Print out each of the outputs

    # Print out 2 articles from each source
    print(PhillyNews.getArticles(2))
    print(PittNews.getArticles(2))

    # Get weather from both cities
    print(PittWeather.getPittWeather())
    print(PhillyWeather.getPhillyWeather())
    
    # TODO - print out sport info
    