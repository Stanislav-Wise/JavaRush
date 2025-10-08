from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class PingAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):

        is_auth = request.user.is_authenticated
        user_repr = str(request.user)
        version = 'v1'
        client_accept = request.headers.get('Accept', '')

        payload = {
            'status': 'ok',
            'message': 'pong',
            'version': version,
            'authenticated': is_auth,
            'user': user_repr,
            'accept': client_accept,
        }

        return Response(payload, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        echo_value = request.data.get('echo')
        payload = {
            'status': 'ok',
            'echo': echo_value,
        }
        return Response(payload, status=status.HTTP_200_OK)