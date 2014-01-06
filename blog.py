import urllib
import webapp2

import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):

  def get(self):
    """Handle GET requests."""

    template_values = {
        'time': '3am Saturday, 29th February',
    }

    template = jinja_environment.get_template('index.html')
    self.response.out.write(template.render(template_values))


APP = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
