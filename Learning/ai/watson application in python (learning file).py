import sys
import requests
import json
import operator
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights 

#This function is used to receive and analyze
def analyze(handle):

	consumer_key = ''
    consumer_secret = ''
	access_token = ''
	access_secret = ''


#This function is used to compare the results from
#the Watson PI API 
  def compare(dict1, dict2):
	compared_data = {}
	for keys in dict1:
    		if dict1[keys] != dict2[keys]:
				compared_data[keys] = abs(dict1[keys] - dict2[keys])
	return compared_data
  
