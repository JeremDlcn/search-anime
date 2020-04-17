from flask import Flask, render_template, redirect, url_for
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def get_source(name):
	name = name.replace('-', '+')
	#setup parser
	print(name)
	source = requests.get(f'https://www.nautiljon.com/animes/{name}.html').text
	soup = BeautifulSoup(source, 'lxml')
	isValid = True
	if soup.find("meta", attrs={"content": "La page spécifiée n'existe pas"}) is None:
		return isValid == True, soup
	else:
		return isValid == False, soup


def get_infos(name, speed, soup):


	#get usual name
	try:
		anime_name = soup.find("h1", class_="h1titre").find("span", attrs={"itemprop": "name"}).text
	except:
		anime_name = '🕵️‍♂️ Anime not found, essayer avec un autre nom'

	#get japanese name
	try:
		anime_jap = soup.find("ul", class_="mb10").find("span", string='Titre original : ').next_sibling  #regex pour detect les kana
	except:
		anime_jap = ''

	#get date
	try:
		date_start = soup.find("ul", class_="mb10").find("span", attrs={"itemprop": "datePublished"}).text
		date_stop = soup.find("ul", class_="mb10").find("span", attrs={"itemprop": "datePublished"}).next_sibling
		anime_date = date_start + date_stop
	except:
		anime_date = 'Inconnu'


	anime_web = []
	try:
		anime_site = soup.find("ul", class_="mb10").find("span", string='Simulcast / streaming : ').parent.find_all('a')
		#sort streaming platform
		for item in anime_site:
			anime_web.append(item.text)
	except:
		anime_site = ['unknown']
	
	#get link to the first episode
	links = []
	try:
		anime_links = soup.select(" .nav_vols > div")
		for link in anime_links:
			episode = link.find("a", attrs={"rel": "nofollow"}).get('href')
			links.append(episode)
	except:
		pass


		
	#group lists of name and link of website
	anime_list = zip(anime_web,links)

	#set the title of the page
	title = anime_name
	
	if speed:
		anime_img =''
		# anime_img = "http://nautiljon.com" + soup.find("a", attrs={"title": "Affiche Originale"}).get('href')
		return title, anime_name, anime_jap, anime_date, anime_site, anime_list, anime_img
	else:
		anime_req =''
		# anime_req = "http://nautiljon.com" + soup.find("a", attrs={"title": "Affiche Originale"}).get('href')
		return title, anime_name, anime_jap, anime_date, anime_site, anime_list, anime_req



def get_img(name_anime):
	view = requests.get(f"https://api.jikan.moe/v3/search/anime?q={name_anime}&limit=1").json()
	get_id = view['results'][0]["mal_id"]
	img = requests.get(f"https://api.jikan.moe/v3/anime/{get_id}/pictures").json()
	get_img = img['pictures'][len(img['pictures'])-1]['large']
	return get_img




@app.route('/')
def index():
	return render_template("index.html", first=True, title='Anime Search')



@app.route('/v1/view/<name>')
def see(name):
	first=False
	isValid, soup = get_source(name)
	if not isValid:
		return redirect(url_for('index'))
	title, anime_name, anime_jap, anime_date, anime_site, anime_list, anime_img = get_infos(name, True, soup)
	return render_template("result.html", **locals())



@app.route('/v2/view/<name>')
def view(name):
	if name == '-' or name == '' or name == '+' or isinstance(name,int):
		return redirect(url_for('index'))
	
	first=False
	isValid, soup = get_source(name)
	print(isValid)
	if not isValid:
		return redirect(url_for('index'))

	title, anime_name, anime_jap, anime_date, anime_site, anime_list, anime_req = get_infos(name, False, soup)

	#get image
	try:
		search_anime = name.replace('-', ' ')
		anime_img = get_img(search_anime)
	except:
		anime_img = anime_req

	return render_template("result.html", **locals())



if __name__ == '__main__':
	app.run()