from pygoogle import pygoogle
import webbrowser
def google_query(query):
	
	g = pygoogle(query) 
	g.pages=1
	g.rsz = 4
	results = {}
	results = g.search()
	rl = results.keys()

	print rl
	

	s = rl[0]
	s.encode('utf-8')
	return s
	
def openUrl(url):
	webbrowser.open(url, new=2, autoraise=True)


