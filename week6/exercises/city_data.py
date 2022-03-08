from urllib import response
import requests
from zipfile import ZipFile
import tqdm
import tarfile

url = 'http://bulk.openweathermap.org/sample/city.list.json.gz'

res = requests.get(url, stream=True)

with open('sample/city.list.json.gz', 'wb') as text_file:
    for chunk in tqdm(response.iter_content(chunk_size=1024)):
        text_file.write(chunk)

with tarfile.open('sample/city.list.json.gz') as tf:
    for m in tf.getnames():
        print(m)
    lst = tf.extractall()