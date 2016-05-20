from bs4 import BeautifulSoup
import re
import urllib2

movie = raw_input("Enter name of movie: ")
search = '+'.join(movie.split())
url = 'http://www.imdb.com/find?q='+search+'&s=all'


response = urllib2.urlopen(url)
page_source = response.read()

search_results = BeautifulSoup(page_source, "lxml")
result_table = search_results.find("table", {"class" : "findList"})
result = result_table.findAll("a")
link = result[1]['href']
print "Title: " + result[1].text

response = urllib2.urlopen('http://www.imdb.com/' + link)
page_source = response.read()

soup = BeautifulSoup(page_source, "lxml")
table = soup.find("table", {"class" : "cast_list"})
cast = table.findAll("span", {"class" : "itemprop"})

print "Cast:"
for actor in cast:
	print actor.text
