from threading import Thread
import requests


class Getter(Thread):
    res = []

    def __init__(self, url):
        self.THE_URL = url
        super().__init__()

    def run(self):
        response = requests.get(self.THE_URL)
        Getter.res.append(response.json())


threads = []
for i in range(10):
    thread = Getter('https://binaryjazz.us/wp-json/genrenator/v1/genre/')
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(Getter.res)
