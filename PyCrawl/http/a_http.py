from typing import Tuple
import aiohttp


class AsyncHttpRequest:
    async def get(self, url, redirect=True, params=None) -> Tuple[any, any]:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=str(url), allow_redirects=bool(redirect), params=params) as response:
                return response, session.cookie_jar

    async def post(self, url, data=None, json=None) -> Tuple[any, any]:
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, data=data, json=json) as response:
                return response, session.cookie_jar

    async def put(self, url, data=None) -> Tuple[any, any]:
        async with aiohttp.ClientSession() as session:
            async with session.put(url=url, data=data) as response:
                return response, session.cookie_jar

    async def delete(self, url) -> Tuple[any, any]:
        async with aiohttp.ClientSession() as session:
            async with session.delete(url=url) as response:
                return response, session.cookie_jar

    async def head(self, url, redirect=True) -> Tuple[any, any]:
        async with aiohttp.ClientSession() as session:
            async with session.head(url=url, allow_redirects=redirect) as response:
                return response, session.cookie_jar

    async def options(self, url, redirect=True) -> Tuple[any, any]:
        async with aiohttp.ClientSession() as session:
            async with session.options(url=url, allow_redirects=redirect) as response:
                return response, session.cookie_jar

    async def patch(self, url, data=None) -> Tuple[any, any]:
        async with aiohttp.ClientSession() as session:
            async with session.patch(url=url, data=data) as response:
                return response, session.cookie_jar
