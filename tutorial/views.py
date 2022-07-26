from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_oso.decorators import authorize_request

@api_view(('GET',))
@authorize_request
def api_test(self, request):
    print(request)
    content = {'message': 'Testing oso integration with drf!'}
    return Response(content)
