from webplucker import *

#db = plucker(['https://httpbin.org/ip'])
#db.timeout = 7
#db.verbose = True
#db.proxy = True

# data = db.cssselect(
#     {
#         'title':'#firstHeading@$text',
#         'sub':'#siteSub@$class'
#     }
#    )

#data = db.xpath('/html/body/div[3]/div[3]/div[5]/div[1]/div[4]/ul/li[3]/ul/li[3]/ul/li[1]/a/span[2]@$text')

# data = db.xpath(
#     {'title':'//*[@id="firstHeading"]@$text',
#      'paragraph':'/html/body/div[3]/div[3]/div[5]/div[1]/p[3]@$text'
#     }
# )

#for x in data:
#print(db.get().text_content())
pl = plucker(['https://www.imdb.com/title/tt0167260/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=EVHJZCG50HQHVAAG7E0B&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_7'])


#pl.render_js = True

data = pl.cssselect({
  'title':'h1@$text',
  'rating': 'span[itemprop="ratingValue"]',
  'starts':'#title-overview-widget > div.plot_summary_wrapper > div.plot_summary > div:nth-child(4) a[href^="/name"] @$text'
})

print(data)