from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


# def get_img(name_anime):
# 	view = requests.get(f"https://api.jikan.moe/v3/search/anime?q={name_anime}&limit=1").json()
# 	get_id = view['results'][0]["mal_id"]
# 	img = requests.get(f"https://api.jikan.moe/v3/anime/{get_id}/pictures").json()
# 	get_img = img['pictures'][len(img['pictures'])-1]['large']
# 	return get_img



@app.route('/')
def index():
	return render_template("index.html", first=True, title='Anime Search')



@app.route('/view/<name>')
def view(name):
	first=False
	#setup parser
	source = requests.get(f'https://www.nautiljon.com/animes/{name}.html').text
	soup = BeautifulSoup(source, 'lxml')

	#get image
	# named = name.replace('+', ' ')
	# anime_img = get_img(named)

	#get informations
	anime_name = soup.find("h1", class_="h1titre").find("span", attrs={"itemprop": "name"}).text
	anime_jap = soup.find("ul", class_="mb10").find("span", string='Titre original : ').next_sibling  #regex pour detect les kana
	date_start = soup.find("ul", class_="mb10").find("span", attrs={"itemprop": "datePublished"}).text
	date_stop = soup.find("ul", class_="mb10").find("span", attrs={"itemprop": "datePublished"}).next_sibling
	anime_date = date_start + date_stop
	anime_site = soup.find("ul", class_="mb10").find("span", string='Simulcast / streaming : ').parent.find_all('a')  #anime_site[0].text

	#set the title of the page
	title = anime_name

	return render_template("result.html", **locals())



if __name__ == '__main__':
	app.run()