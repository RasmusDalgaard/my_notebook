from cv2 import split
import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

class TextComparer:
    
    def __init__(self, url_list):
        self.url_list = url_list
        self.file_list = [url.split('/')[-1] for url in url_list]
    
    def download(self, url, filename):
        response = requests.get(url, allow_redirects=True)
        response.raise_for_status()
        open(filename, 'wb').write(response.content)

    def multi_download(self):
      with ThreadPoolExecutor(len(self.url_list)) as ex:
        #Calls the download func on each url in the url_list and uses the file names from the file_list
        ex.map(self.download, self.url_list, self.file_list) 
    
    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index < len(self.file_list):
            file = self.file_list[self.current_index]
            self.current_index += 1
            return file
        raise StopIteration

    def urllist_generator(self):
        for url in self.url_list:
            yield url

    def avg_vowels(self, filename):
        with open(filename) as text:
            total_vowels = 0
            total_chars = 0
            total_words = 0
            lines = list(line for line in (l.strip() for l in text) if line)
            for line in lines:
                for word in line.split(' '):
                    total_words += 1
                    for char in word:
                        total_chars += 1
                        if char in "aeiouAEIOU":
                            total_vowels += 1
        return total_vowels / total_words

    
    def hardest_read(self, workers=multiprocessing.cpu_count()):
        with ProcessPoolExecutor(workers) as ex:
            response = ex.map(self.avg_vowels, self.file_list)
            return max(list(response))




textComp = TextComparer(['https://www.gutenberg.org/files/11/11-0.txt', 'https://www.gutenberg.org/files/1342/1342-0.txt', 'https://www.gutenberg.org/files/345/345-0.txt'])
iterator = iter(textComp)

#textComp.multi_download()

#print(next(iterator))

#tmp_url = textComp.urllist_generator()
#print(next(tmp_url))

#print(textComp.avg_vowels(textComp.file_list[0]))

#print(textComp.hardest_read())


