import os
from django.conf import settings
import rest_framework
from django_oso import oso
from django.contrib.auth.models import User

def django_oso_middleware(get_response):
    # One-time configuration and initialization.
    oso.Oso.load_files(filenames=[os.path.join(settings.BASE_DIR,'snippets','policy','rule.polar') ])
    oso.Oso.register_class(User)
    oso.Oso.register_class(rest_framework.request.Request)

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # print(request.user.username)
        # oso.Oso.authorize_request(request.user,request)
        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        if response.status_code == 403:
            print(request.path)

        return response

    return middleware
