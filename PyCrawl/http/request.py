from PyCrawl.http.methods import PyCrawlMethods
from PyCrawl.http.pwb_http import PyWebRequest
from PyCrawl.http.a_http import AsyncHttpRequest
from PyCrawl.exceptions import InvalidMethod


class Request:
    def __int__(self, url: str, method: PyCrawlMethods, params: dict = None, data: dict = None, json: dict = None, redirect: bool = True):
        self.url = url
        self.method = method
        self.redirect = redirect
        self.params = params
        self.data = data
        self.json = json
        self.pw_req = PyWebRequest()
        self.ah_req = AsyncHttpRequest()

    async def _execute(self):
        if self.method == PyCrawlMethods.PW_GET:
            return await self.pw_req.get(self.url)
        elif self.method == PyCrawlMethods.AH_GET:
            return await self.ah_req.get(url=self.url, redirect=self.redirect, params=self.params)
        elif self.method == PyCrawlMethods.AH_POST:
            return await self.ah_req.post(url=self.url, data=self.data, json=self.json)
        elif self.method == PyCrawlMethods.AH_PUT:
            return await self.ah_req.put(url=self.url, data=self.data)
        elif self.method == PyCrawlMethods.AH_DELETE:
            return await self.ah_req.delete(url=self.url)
        elif self.method == PyCrawlMethods.AH_HEAD:
            return await self.ah_req.head(url=self.url, redirect=self.redirect)
        elif self.method == PyCrawlMethods.AH_OPTIONS:
            return await self.ah_req.options(url=self.url, redirect=self.redirect)
        elif self.method == PyCrawlMethods.AH_PATCH:
            return await self.ah_req.patch(url=self.url, data=self.data)
        else:
            raise InvalidMethod(self.method)
