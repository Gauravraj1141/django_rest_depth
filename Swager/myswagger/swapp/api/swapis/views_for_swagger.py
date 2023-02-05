from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from swapp.serializer import NotificationSerializer
from swapp.models import Notification

from drf_yasg.utils import swagger_auto_schema
from swapp.api.swapis.documetation_swagger import *


class NotiData(GenericAPIView):
    serializer_class = NotificationSerializer

    @swagger_auto_schema(
        tags=["User Property APIs"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=REQUIRED_LIST,
            properties=INPUT_PROPERTIES_DESCRIPTION),
        responses=RESPONSE_DESCRIPTION
    )
    # def get(self, request):
    #     # import pdb
    #     # pdb.set_trace()
    #     objects = Notification.objects.all()
    #     serialize = NotificationSerializer(objects, many=True)
    #     return Response(serialize.data)
    def post(self, request):
        data = request.data
        input_json = dict(zip(["name", "email"], [data['user creadentials']['Create User']
                          ["name"], data['user creadentials']['Create User']["email"]]))
        print(input_json['name'], input_json['email'], input_json)
        datafill = Notification.objects.create(
            name=input_json['name'], email=input_json['email'], )
        return Response("Successfully Added ")


# class deletedata(GenericAPIView):
#     serializer_class = NotificationSerializer

#      request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             required=REQUIRED_LIST,
#             properties=INPUT_PROPERTIES_DESCRIPTION),
#         responses=RESPONSE_DESCRIPTION
#     )

#     def delete(self, request):
#         data = request.data
#         ourdata = Notification.objects.get(id=data["id"])
#         ourdata.delete()
#         return Response("successfully delte")
