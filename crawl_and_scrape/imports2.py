from selenium.webdriver.common.keys import Keys
import webbrowser
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import sqlite3
import inspect
import re
import time
import Just_titles

DBName = 'IMDB.db'
conn = sqlite3.connect(DBName) # this must need changing.
cursor = conn.cursor()
i = 'Alexs_little_film'
name = 'Patricia_The_Programer'

cursor.execute(f'''
INSERT INTO PM (title, ProductionManager)
VALUES('{i}', '{name}');
''')

conn.commit()
conn.close()

