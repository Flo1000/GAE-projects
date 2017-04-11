from google.appengine.ext import ndb

class Movie(ndb.Model):
    # data model for a movie:
    #      - contains movie title, rating and a link to a picture

    name = ndb.StringProperty()
    rating = ndb.IntegerProperty()
    piclink = ndb.StringProperty()

# allmovies = ndb.Query(Movie)
# allmovies.order(-allmovies.rating)