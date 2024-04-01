import os
import requests
from requests.auth import HTTPBasicAuth
import json
from bs4 import BeautifulSoup as BS

url = "https://<YOUR_ORGANIZATION>.atlassian.net/wiki/rest/api/content/10940186625?expand=body.storage"

auth = HTTPBasicAuth("ashishkarev@<YOUR_ORGANIZATION>.com", os.environ.get('CONFLUENCE_TOKEN'))

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

def content_parse(macro_id):
	html = BS(response.content, 'html.parser')
	items = html.find_all('ac:structured-macro')
	for item in items:
		if item.get('ac:macro-id') == f'\\"{macro_id}\\"':
			return [
				sql for sql in item.find('ac:plain-text-body')
			][0].replace('\\n', '').replace('\\', '')
