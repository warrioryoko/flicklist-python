import webapp2

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles

        # TODO: randomly choose one of the movies, and return it

        return "The Big Lebowski"

    def get(self):
        movie = self.getRandomMovie()

        # build the response string
        response = "<h1>Movie of the Day</h1>"
        response += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"

        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
