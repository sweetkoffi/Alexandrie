PROJET Alexandrie -------------> Heritée du Projet_Hermes_Me_V3 by Sweetkoffi and J-devx

    ## Config.txt ( gitignore ) -------------> stock API key 

    ## Fonction HermesNewsApi : Utilise NEWS-API , et fait une recherche via le endpoint "/everything afin de trouver
    les articles correspondant au mot clee rentrer via le prompteur. Verifie seulement les articles publier dans les derniers
    24h. ( Clee API lue a partir du fichier config.tx ) " 


    ## Fonction Alexandrie : 
        - Option 1 - Package "google_scholar_py" -------------> need Chrome to be available on the machine used (AppData\Local\Google\Chrome\Application\chrome.exe)
            - Back end use selenium  -------------> Option Abandonne
    
        - Option 2 - SERP-API key ( 100 search by day )
            - need : pip install google-search-results -------------> Option retenue 

Requirements 

    - configparser
    - requests
    - json
    - rich ( table , console )
    - google-search-results

