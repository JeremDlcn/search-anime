from flask import Flask, render_template, redirect, url_for
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)

def get_source(name):
	#setup parser
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
		anime_name = '🕵️‍♂️ Anime non trouvé, essayer avec un autre nom'
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
	#get website
	anime_web = []
	try:
		anime_site = soup.find("ul", class_="mb10").find("span", string='Simulcast / streaming : ').parent.find_all('a')
		#sort streaming platform
		tmp =''
		for item in anime_site:
			if item.text == 'J-One':
				tmp = item.text
			else:
				anime_web.append(item.text)
		if tmp != '':
			anime_web.append(tmp)
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
		try:
			anime_img = "http://nautiljon.com" + soup.find("a", attrs={"title": "Affiche Originale"}).get('href')
		except:
			anime_img = ""
		finally:
			return title, anime_name, anime_jap, anime_date, anime_site, anime_list, anime_img
	else:
		try:
			anime_req = "http://nautiljon.com" + soup.find("a", attrs={"title": "Affiche Originale"}).get('href')
		except:
			anime_req = ""
		finally:
			return title, anime_name, anime_jap, anime_date, anime_site, anime_list, anime_req


def get_img(name_anime):
	view = requests.get(f"https://api.jikan.moe/v3/search/anime?q={name_anime}&limit=1").json()
	get_id = view['results'][0]["mal_id"]
	img = requests.get(f"https://api.jikan.moe/v3/anime/{get_id}/pictures").json()
	get_img = img['pictures'][len(img['pictures'])-1]['large']
	return get_img




@app.route('/')
def index():
	return render_template("index.html", clip=False, first=True, title='Anime Search')

@app.route('/robots.txt')
def robots():
	return redirect(url_for('static', filename='robots.txt'))

@app.route('/googlee7946324b3d5277b.html')
def property():
	return redirect(url_for('static', filename='googlee7946324b3d5277b.html'))

@app.route('/v1/view/<name>')
def see(name):
	if name == '-' or name == '' or name == '+':
		return redirect(url_for('index'))
	res=True
	clip=True
	isValid, soup = get_source(name)
	if not isValid:
		return redirect(url_for('index'))
	title, anime_name, anime_jap, anime_date, anime_site, anime_list, anime_img = get_infos(name, True, soup)
	return render_template("result.html", **locals())



@app.route('/v2/view/<name>')
def view(name):
	if name == '-' or name == '' or name == '+':
		return redirect(url_for('index'))
	
	res=True
	clip=True
	isValid, soup = get_source(name)
	if not isValid:
		return redirect(url_for('notfound'))
	title, anime_name, anime_jap, anime_date, anime_site, anime_list, anime_req = get_infos(name, False, soup)

	#get image
	try:
		search_anime = name.replace('-', ' ')
		anime_img = get_img(search_anime)
	except:
		anime_img = anime_req

	return render_template("result.html", **locals())



@app.route('/search/<name>')
def search(name):
	ser = True
	title = name.replace('-', ' ')
	name = name.replace('-', '+')
	#setup search parser
	search_source = requests.get(f'https://www.nautiljon.com/animes/?q={name}').text
	s_soup = BeautifulSoup(search_source, 'lxml')
	search_list = []
	try:
		element = s_soup.select_one('table.search.liste').find('tbody').find_all('tr')
		for item in element:
			disc = {}
			disc['link'] = item.find('td', class_="image").find('a').get('href').replace('/animes/','/v2/view/').replace('.html', '')
			disc['img'] = "http://nautiljon.com" + item.find('td', class_="image").find('img').get('src')
			disc['name'] = item.find('td', class_="left vtop").select_one('td > a').text
			disc['date'] = item.select_one('tr td:nth-of-type(7)').text
			search_list.append(disc)
	except:
		pass
	if len(search_list) > 5:
			flight = True

	return render_template("search.html", **locals())
	


@app.route('/notfound')
def notfound():
	return render_template("notfound.html", title='Anime Introuvable')



@app.errorhandler(Exception)
def error(error):
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run()