from PyWeb.main import get as pw_get


class PyWebRequest:
    async def get(self, url):
        res = await pw_get(url)
        return res
