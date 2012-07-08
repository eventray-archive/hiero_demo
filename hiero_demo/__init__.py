from pyramid.config     import Configurator
from hem.interfaces     import IDBSession
from hiero_demo.models  import DBSession
from sqlalchemy         import engine_from_config

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    config.registry.registerUtility(DBSession, IDBSession)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('favicon', '/favicon.ico')
    config.add_view('hiero_demo.views.favicon_view', route_name='favicon')

    #config.include('hiero', route_prefix='/blog')
    config.include('hiero', route_prefix='blog')

    config.scan()

    return config.make_wsgi_app()
