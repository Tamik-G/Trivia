import requests
import asyncio

async def get():
    return requests.get('https://httpbin.org/get')

async def put():
    return requests.put("https://httpbin.org/put", data={'key': 'value'})

async def delete():
    return requests.delete('https://httpbin.org/delete')

async def post():
    return requests.post("https://httpbin.org/post", data={'key' : "value"})

async def main():
    result = await asyncio.gather(
        get(),
        post(),
        put(),
        delete(),
    )
    for res in result:
        print(res.json()['url'])

asyncio.run(main())