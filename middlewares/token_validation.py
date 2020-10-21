import jwt
import base64
import json
from rest_framework_jwt.utils import jwt_decode_handler
from django.http.response import JsonResponse


token_required = {
    '/api/v1/users/': {'GET': True, 'POST': False},
    '/api/v1/subject/': {'GET': True, 'POST': True},
}


class TokenValidationMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    #@add_entry_exit_logs
    def __call__(self, request):
        if token_required.get(request.path):
            if token_required.get(request.path).get(request.method):
                auth = request.META.get('HTTP_AUTHORIZATION')
                if not auth:
                    return JsonResponse(data={
                        "code": "authorization_header_missing",
                        "description": "Authorization header is expected"},
                        status=401)

                # token = auth.split(' ')[1]

                # # Confirm A JSON Web Token (JWT) includes three sections
                # token_parts = token.split('.')
                # if len(token_parts) != 3:
                #     return JsonResponse(data={"code": "invalid_header",
                #                             "description": "Invalid Token"},
                #                         status=401)

                try:
                    decoded_token = jwt_decode_handler(auth)
                except jwt.ExpiredSignatureError as e:
                    return JsonResponse(data={"code": "invalid_header",
                                            "description": "Token Expired:"
                                                            " %s" % str(e)},
                                        status=401)
                if not request.GET._mutable:
                    request.GET._mutable = True
                    request.GET['query'] = decoded_token
                response = self.get_response(request)
                return response

        else:
            response = self.get_response(request)
            return response

