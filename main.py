import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movie_list =['Pulp Fiction', 'Kill Bill', 'The Matrix', 'Dr. Strange', 'Star Wars: Rogue One']

        # TODO: randomly choose one of the movies, and return it
        rand_selection = random.choice(movie_list)
        return rand_selection

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"

        next_movie = self.getRandomMovie()

        if next_movie == movie:
            next_movie = self.getRandomMovie()
        content += "<h1>Tomorrow's Movie</h1>"
        content += "<p>" + next_movie + "</p>"
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
