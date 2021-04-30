from webplucker import *

db = plucker(['https://en.wikipedia.org/wiki/Proxy_server#:~:text=In%20computer%20networking%2C%20a%20proxy,servers%20that%20provide%20those%20resources.','https://en.wikipedia.org/wiki/Proxy_server#Monitoring_and_filtering'])
db.timeout = 7
db.verbose = True

data = db.cssselect(
    {
        'title':'#firstHeading@$text',
        'sub':'#siteSub@$class'
    }
   )

#data = db.xpath('/html/body/div[3]/div[3]/div[5]/div[1]/div[4]/ul/li[3]/ul/li[3]/ul/li[1]/a/span[2]@$text')

# data = db.xpath(
#     {'title':'//*[@id="firstHeading"]@$text',
#      'paragraph':'/html/body/div[3]/div[3]/div[5]/div[1]/p[3]@$text'
#     }
# )

#for x in data:
print(data)