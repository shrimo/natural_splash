from grab import Grab
from grab.ext import lxml
import google_lib as golib

query='crimea'
#file_out='out1.html'

go_url = golib._url(query)
g = Grab()
#g.go(go_url, log_file=file_out)
g.go(go_url)

print g.css_text('#resultStats')
print '---'
#print g.xpath_text('//*[h3[@class="r"]/a]')
print g.xpath_text('//div [@class="slp"]')
print '---'
#print g.css_text('#search')
#print g.xpath_text('//h2[@class="hd"]')

