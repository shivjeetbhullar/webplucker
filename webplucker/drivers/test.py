import asyncio
from pyppeteer import launch

class engine():
 def __init__(self):
     pass
     
 async def start(self):
     self.browser = await launch({'headless': True})
     self.page = await self.browser.newPage()
 
 async def goto(self,url):
  await self.page.goto(url)
  return await self.page.content()

 async def close(self):
  await self.browser.close()

urls = ['https://accounts.gursurdevelopers.com/class','https://accounts.gursurdevelopers.com/class','https://accounts.gursurdevelopers.com/class']

from multiprocessing import Process

def f(en,x):
    asyncio.get_event_loop().run_until_complete(en.goto(x))

if __name__ == '__main__':
   en = engine()
   asyncio.get_event_loop().run_until_complete(en.start())
   for x in urls:
    print(x)
    p = Process(target=f, args=(en,x,))
    p.start()
  





#asyncio.get_event_loop().run_until_complete(en.close())

# import asyncio
# from pyppeteer import launch

# async def main():
#     browser = await launch({'headless': True})
#     page = await browser.newPage()
#     await page.goto('https://accounts.gursurdevelopers.com/class')
#     content = await page.content()
#     print(content)
    
#     await browser.close()

# asyncio.get_event_loop().run_until_complete(main())

# from flask import Flask
# from multiprocessing import Process
# from requests_html import HTMLSession

# app = Flask(__name__)

# def testfu(r):
#     r.html.render()
#     table = r.html.find('#mainapp', first=True)
#     print(table.text)
#     return table.text

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# @app.route('/test')
# def dshello_world():
#     session = HTMLSession()
#     r = session.get('http://accounts.gursurdevelopers.com/')
#     p = Process(target=testfu, args=(r,))
#     p.start()
#     p.join()
#     return 'testfu'

# app.run()