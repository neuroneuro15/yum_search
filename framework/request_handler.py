import os
import jinja2
from webapp2 import RequestHandler

class YumSearchRequestHandler(RequestHandler):

    template_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                      os.pardir,
                                                      'templates'))

    jinja_environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_directory)
    )

    def render(self, template, **kwargs):

        jinja_template = self.jinja_environment.get_template(template)
        html_from_template = jinja_template.render(kwargs)

        self.response.out.write(html_from_template)