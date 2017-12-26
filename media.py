## MovieWebsite Project ###
## Contents : Titles, StoryLine, Poster_image, youtube_trailer
## creating class and defining init
import webbrowser
class Movie():
#Class Variables can be used here :see Ad.txt
	"""Class has movie related info"""  ##This is predefined variables __doc__
	def __init__(self, movie_title, movie_storyline, poster_image, youtube_trailer):
#this __init__ keyword is reserved and this function is special method to create space for details/contents above.
#self is object created. when class is called object will be self and eg in this case toystory will be self.
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = youtube_trailer
#
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
	