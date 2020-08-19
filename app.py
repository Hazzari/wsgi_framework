#!/usr/bin/env python
# -*- coding: utf-8 -*-

from server import Application


def index_handler(request):
    return {

        "text": "Hello World",
        "extra_headers": {'Content - Type': 'text/plain'}

    }


def contact_handler(request):
    return {
        "json": {'city': 'Moscow',
                 'street': 'Balaclavskiy-pt.'},
    }


application = Application()
application.add_handler("/", index_handler)
application.add_handler("/contacts/", contact_handler)
