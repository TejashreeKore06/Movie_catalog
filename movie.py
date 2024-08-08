class Movie():
    """ This class provides a structure to hold movies information """    
    
    # class constructor
    def __init__(self, movie_title, movie_storyline, release_date, 
    			rating, poster_image, featured_movie, 
    			slider_image_url, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.release_date = release_date
        self.rating = rating
        self.poster_image_url = poster_image
        self.featured_movie = featured_movie
        self.slider_image_url = slider_image_url
        self.trailer_youtube_url = trailer_youtube