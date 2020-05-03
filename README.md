# Anime Search
**Anime Search** est une application Flask de webscraping permettant de savoir sur quelle platforme de streaming légale on peut visionner la série d'animation que l'on recherche.

Les données sont récupérées depuis le site de [Nautiljon](https://www.nautiljon.com/).

![Page accueil](https://cloud-image-dlcn.netlify.com/anime-search/home.png)

Le lien vers le site [Anime Search](https://search-anime.herokuapp.com/).

Cette application m'a permis d'apprendre à faire du webscraping et de m'améliorer en Flask.

## Fonctionnement
L'application possède 3 pages:
- La page d'*accueil* permettant de rechercher une série.
- La page d'*affichage des résultats* qui montre les résultats correspondant à notre recherche.
- La page de *détails* d'une série, où l'on peut voir des informations sur la série.

L'application permet aussi de visualiser le détail d'une série plus rapidement au détriment de la qualité d'image en activant le bouton *"Speed Mode"* dans la page de recherche.


## Technologies utilisées
- Le micro-framework Flask
- Le langage Python 3.8
- L'installeur de paquets pip 20.1
- Bibliothèque Python :
	- Beautiful Soup 4 (Webscraping)
	- lxml (Parser)
	- requests (requête HTTP)
	- gunicorn (déploiement en production)
## Déploiement de l'application
L'application à été déployé sur [Heroku](https://heroku.com) qui permet de déployer gratuitement des applications webs (NodeJS, Python, Java, Go, PHP, ...)
