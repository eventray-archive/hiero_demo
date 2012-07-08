import os
from pyramid.response import FileResponse
from pkg_resources      import resource_filename

def favicon_view(request):
    fname = resource_filename(__name__, '../static/favicon.ico')
    return FileResponse(fname, request=request)
