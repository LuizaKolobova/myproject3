from wsgiref.simple_server import make_server
from jinja2 import Environment,FileSystemLoader
from pyramid.response import *
from pyramid.config import *
enviroment=Environment(loader=FileSystemLoader("htmkfiles"))

def Index(request):
    return Response(enviroment.get_template('/index.jinja2').render(link1='<h3> <a href="http://localhost:8000/about/aboutme.html">Абсолютная ссылка</a> </h3>',
                                                         link2='<h3> <a href="/about/aboutme.html">Относительная ссылка </a></h3>',color='{color: #FF1493;}',
                                                         text ='<h1><i>Ссылки на  aboutme.html </i> </h1>'))
def Aboutme(request):
    return Response(enviroment.get_template('/aboutme.jinja2').render(link1='<h3> <a href="http://localhost:8000/index.html">Абсолютная ссылка</a> </h3>',
                                                         link2='<h3><a href="/index.html">Относительная ссылка </a></h3>',color='{color: #FFFF00;}',
                                                         text ='<h1><i>Ссылки на index.html </i> </h1>'))

if __name__ == "__main__":
    config=Configurator()
    config.add_view(Index, route_name="home")
    config.add_route("home", "/")
    config.add_view(Index, route_name="index")
    config.add_route("index", "/index.html")
    config.add_view(Aboutme, route_name="aboutMe")
    config.add_route("aboutMe", "/about/aboutme.html")
    app=config.make_wsgi_app()
    server = make_server("localhost", 8000, app)
    print ("Serving localhost on port 8000...")
    server.serve_forever()

