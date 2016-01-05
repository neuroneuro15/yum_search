from webapp2 import WSGIApplication
from webapp2 import Route


app = WSGIApplication(
    routes=[
        Route('/', handler='')
    ]
)