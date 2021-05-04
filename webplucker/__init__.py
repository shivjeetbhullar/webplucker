from .req_handler import *
from .jsengine import engine
import asyncio

class plucker:
    def __init__(self,urls):
        self.urls = urls
        self.requests = 10
        self.timeout = 5
        self.verbose = True
        self.organised = False
        self._render_js = False
        
    @property
    def render_js(self):
        return self._render_js

    @render_js.setter
    def render_js(self, new_value):
       if new_value:
           en = engine()
           self.engine = en
           asyncio.get_event_loop().run_until_complete(self.engine.start())
       self._render_js = new_value
    
    def cssselect(self,tag):
        if self.render_js:return jsreq(tag,self,'css')
        else:return req(tag,self,'css')
    
    def xpath(self,tag):
        if self.render_js:return jsreq(tag,self,'xpath')
        else:return req(tag,self,'xpath')
    
    def get(self):
        if self.render_js:return jsreq(tag,self,'None')
        else:return req('None',self,'None')
    
