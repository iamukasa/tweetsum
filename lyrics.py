from bs4 import BeautifulSoup
import requests
import sys
import textsummariser as summarise
URL = str(sys.argv[1])
page = requests.get(URL)    
html = BeautifulSoup(page.text, "html.parser") # Extract the page's HTML as a string

# Scrape the song lyrics from the HTML
lyric =str( html.find("div", class_="lyrics").get_text().encode('ascii','ignore'))
lyrics=lyric.replace ('\n','.').replace('\n\n','.')
thesummarised=summarise.FrequencySummariser().summarize(lyrics.strip(),1)
print ( "and the summary is ",thesummarised)
