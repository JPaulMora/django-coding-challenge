from django.http.response import JsonResponse
from django.views import generic
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView


class IndexView(generic.TemplateView):
    template_name = "index.html"


class ProductListView(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be listed.
    """

    # TODO Your view code here


class OrderView(APIView):
    parser_classes = (JSONParser,)
    authentication_classes = []

    def post(self, request):
        """
        API endpoint that calculates the order total.
        """
        print(request.data)

        response_obj = {"total": 0}

        # TODO Calculate the order total here

        return JsonResponse(response_obj, safe=False)
