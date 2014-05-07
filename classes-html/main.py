
import webapp2
from pages import Page #from pages file import Page class

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.body = 'Miss Piggy likes Kermit de Frog'
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
