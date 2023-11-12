#########################################################
#  Projet : Alexandrie                                  #
#  last update : 2023-08-09                             #
#  Author : SweetKoffi                                  #
#                                                       #
#########################################################
import requests
import json
import configparser
from rich.console import Console
from rich.table import Table
from datetime import datetime , timedelta
#from google_scholar_py import CustomGoogleScholarProfiles ---> Option 1
from serpapi import GoogleSearch 
yesterday = datetime.now() - timedelta(days = 1)
######################################################### Config file 
# objet de config
#config = configparser.ConfigParser()
# Lire fichier de config
#config.read('config.txt')
# Accéder aux API KEYS
import constants

news_api_key = constants.news_api_key
serapi_api_key = constants.serapi_api_key
######################################################### LOGO
logo = '''                                          
    ___    __                          __     _  
   /   |  / /__  _  ______ _____  ____/ /____(_)__ 
  / /| | / / _ \| |/_/ __ `/ __ \/ __  / ___/ / _ |
 / ___ |/ /  __/>  </ /_/ / / / / /_/ / /  / /  __/
/_/  |_/_/\___/_/|_|\__,_/_/ /_/\__,_/_/  /_/\___/                                                    
                                  _______________           
                                 |               |
                                 | By SweetKoffi | 
                                 |_______________|'''

# Taille du rectangle 
lines = logo.split("\n")
width = max(len(line) for line in lines)

# Haut et bas du rectangle
top_border = "+" + "-" * (width + 2) + "+"
bottom_border = "+" + "-" * (width + 2) + "+"

# Imprimer ASCII rectangle art
def print_logo():
    print(top_border)
    for line in lines:
        padding = " " * (width - len(line))
        print("| " + line + padding + " |")
    print(bottom_border)

######################################################### Rich Table
console = Console()
table = Table(title="Alexandrie by SweetKoffi")
table.add_column("Results", justify="left",width=70, style="cyan")
'''table.add_column("Author",width=30, style="magenta")
table.add_column("URL",width=70, justify="left", style="green")'''
########################################################## Option 1
#def ScholarGoogle(): 
    #parser = CustomGoogleScholarProfiles()
    #data = parser.scrape_google_scholar_profiles(
    #    query='Intelligence artificielle',
    #    pagination=False,
    #    save_to_csv=False,
    #    save_to_json=False
    #)
    #print(json.dumps(data, indent=2))
########################################################## Option 2
def ScholarGoogle (keyword_search_google): 
    #base_url = 'https://serpapi.com/search.json?engine=google_scholar'
    #https://serpapi.com/search.json?engine=google_scholar&q=biology
    params = {
    "engine": "google_scholar",
    "q": keyword_search_google,
    "api_key": serapi_api_key
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    #print(type(results))
    #organic_results = results["organic_results"]
    resultats_json = json.dumps(results)
    resultats_loaded = json.loads(resultats_json)
    organic_resultats_json = resultats_loaded["organic_results"]
    #### Add to rich table 
    for article in organic_resultats_json:
        infosup = article['publication_info']
        table.add_row("[link="+article['link']+"]"+article['title']+"[/link]",style="bold green")
        table.add_row(infosup['summary'])
        table.add_row(' ')
#########################################################  Fonction HermesNewsApi
def HermesNewsApi(keyword,date):
    base_url = 'https://newsapi.org/v2/everything?'
    sort_by = 'popularity'
    api_key = news_api_key
    #print(api_key)
    url = f"{base_url}q={keyword}&from={date}&sortBy={sort_by}&apiKey={api_key}"
    #print(url)
    response = requests.get(url)
    #json_response = json.dumps(response)
    json_response = response.json()
    resultats = json_response['articles']
     #### Add to rich table  
    for article in resultats:
        #print(article)
        raw_date_str = article.get('publishedAt', '') or ''
        #article['publishedAt']
        title = article.get('title', '') or ''
        #article['title']
        description = article.get('description', '') or ''
        #article['description']
        author = article.get('author', '') or ''
        #article['author']
        link = article.get('url', '') or ''
        #article['url']
        fixed_date = datetime.strptime(raw_date_str, '%Y-%m-%dT%H:%M:%SZ')
        readable_date = fixed_date.strftime('%B %d, %Y at %H:%M:%S')
        #print("+" + "-" * (width + 2) + "+")
        table.add_row("[link="+link+"]"+title+"[/link]" , style="bold green")
        table.add_row(description)
        table.add_row(readable_date , style="italic green")
        table.add_row(author, style="magenta")
        table.add_row(' ')
        #table.add_row('-'*70 ,'-' * 30, '-'*70)
###############
keyword = input('Entrez le keyword : ')
date    = yesterday.strftime("%y%m%d")
###############
print_logo()
HermesNewsApi(keyword,date)
ScholarGoogle(keyword)
console.print(table)

