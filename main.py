import threading
from datetime import timedelta

import httpx
import redis

con = redis.Redis(host='localhost', port=6379, decode_responses=True)
threads = {
    'oqim1': 'https://daryo.uz',
    'oqim2': 'https://github.com',
    'oqim3': 'https://hub.docker.com',
    'oqim4': 'https://www.mediafire.com/',
    'oqim5': 'https://www.youtube.com'
}

def response(thread_name, url):
    response = httpx.get(url)
    con.set(name=thread_name, value=response.text, ex=timedelta(seconds=60))


for thread_name, url in threads.items():
    thread = threading.Thread(target=response, args=(thread_name, url))
    thread.start()

for thread in threading.enumerate():
    if thread != threading.current_thread():
        thread.join()
