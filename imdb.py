from bs4 import BeautifulSoup
import re
import urllib2

#Taking input from user for movie name
movie = raw_input("Enter name of movie: ")
#Changing spaces to +
search = '+'.join(movie.split())
#Creating search url for IMDB
url = 'http://www.imdb.com/find?q='+search+'&s=all'

#Using urllib to get page source for above url
response = urllib2.urlopen(url)
page_source = response.read()

#Parsing the page source to Beautiful Soup
search_results = BeautifulSoup(page_source, "lxml")
try:	
	#Finding search results table, and retrieving first result
	result_table = search_results.find("table", {"class" : "findList"})
	#result is an array containing all <a> tagged elements
	result = result_table.findAll("a")
	#Finding first link (Index 0 corresponds to Image of the result. Index 1 contains Title). Storing relative address in link
	link = result[1]['href']
	print "Title: " + result[1].text
except:
	print "No results found for " + movie
	exit()

#Getting page source for First Result
response = urllib2.urlopen('http://www.imdb.com/' + link)
page_source = response.read()

#Parsing using BeautifulSoup
soup = BeautifulSoup(page_source, "lxml")
try:
	#Finding cast list table
	table = soup.find("table", {"class" : "cast_list"})
	#Retrieving and printing constituent items
	cast = table.findAll("span", {"class" : "itemprop"})

	print "Cast:"
	for actor in cast:
		print actor.text
except:
	print "No cast found for" + result[1].text
	exit()