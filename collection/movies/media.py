import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    
    #generic (CONSTANT) variable for the class
    #VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    #Function that initializes or creates space in memory for new instance
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #particular variables for each instance
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
