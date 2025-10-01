import os
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns


#Paso 1
resource_url = " https://en.wikipedia.org/wiki/List_of_most-streamed_songs_on_Spotify"
response = requests.get(resource_url, time.sleep(3))

#Paso 2
response
