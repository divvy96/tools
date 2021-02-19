import aiohttp

import asyncio

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            t = asyncio.create_task(download(session, url))
            tasks.append(t)
            print("trying: " + url)
        await asyncio.gather(*tasks)

    for t in tasks:
        print(t.result())

async def download(session, url):
    async with session.get(url) as response:
        content = await response.read()
        return content

if __name__ == '__main__':
    urls = ['http://google.co.uk', 'http://yahoo.com', 'http://facebook.com']
    asyncio.run(main(urls))
