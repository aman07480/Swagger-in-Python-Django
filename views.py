from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class HelloAPI(APIView):

    @swagger_auto_schema(
        operation_description="Simple hello API",
        responses={200: openapi.Response(description="Returns greeting message")}
    )
    def get(self, request):
        return Response({"message": "Hello Swagger!"})
