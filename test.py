import urllib.request
import requests


url = "https://docs.google.com/document/u/0/d/1GNIOZ3UB0PY7xHQlbZDCHQX9rju8yrtMt7CjFAIAgQg/export?format=docx"

u = urllib.request.urlopen(url)

meta = u.info()

print(meta)



for i,j in meta.items():
	print(i + " : " + j)
	print( )

