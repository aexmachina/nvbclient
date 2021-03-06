from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('key_details', '/details')
    config.add_route('update_utxos', '/update_utxos.json')
    config.add_route('sign_vote', '/sign_vote.json')
    config.add_route('initialize_network', '/initialize_network.json')
    config.add_route('check_password', '/check_password.json')
    config.add_route('change_password', '/change_password.json')
    config.add_route('demo_test', '/demo_test.json')
    config.add_route('empower_demo', '/empower_demo.json')
    config.add_route('empower_demo_start', '/empower_demo_start.json')
    config.scan()
    return config.make_wsgi_app()
