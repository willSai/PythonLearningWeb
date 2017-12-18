' url handlers '

from coroweb import get
import asyncio

@get('/')
async def index(request):
    return '<h1>Hi, Qian</h1>'

@get('/hello')
async def hello(request):
    return '<h1>hello!</h1>'