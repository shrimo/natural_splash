from grab import Grab
from grab.ext import lxml
import google_lib as golib
from grab.tools.lxml_tools import get_node_text

query='habrahabr'
#file_out='out1.html'

go_url = golib._url(query,page=1)
g = Grab()
#g.go(go_url, log_file=file_out)
g.go(go_url)

print g.css_text('#resultStats')
print '---'
f = open('data_file.txt','a')
for elem in g.xpath_list('//div [@id="ires"]'):
    for i in range(len(elem.xpath('//span [@class="f nsa"]'))):
        title_elem = elem.xpath('//span [@class="f nsa"]')[i]
        data = get_node_text(title_elem, smart=False)
        #if (data[:1]!='1'):
        print 'out->',data
        f.write(data+'\n')

f.close()

print '---'
#print g.xpath_list('//span [@class="f nsa"]')




#print g.css_text('#search')
#print g.xpath_text('//h2[@class="hd"]')
#print g.xpath_text('//*[h3[@class="r"]/a]')

