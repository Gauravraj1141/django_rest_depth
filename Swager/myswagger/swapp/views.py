# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.generics import GenericAPIView 
# from .serializer import NotificationSerializer
# from .models import Notification

# from drf_yasg.utils import swagger_auto_schema


# class NotiData(GenericAPIView):
#     serializer_class = NotificationSerializer
#     @swagger_auto_schema(
#         tags=["User Property APIs"],
#         manual_parameters=[HEADER_PARAMS['access_token']],
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             required=REQUIRED_LIST,
#             properties=INPUT_PROPERTIES_DESCRIPTION),
#         operation_description=OPERATIONS_DESCRIPTION,
#         responses=RESPONSE_DESCRIPTION
#     )

#     def get(self, request):
#         # import pdb
#         # pdb.set_trace()
#         objects = Notification.objects.all()
#         serialize = NotificationSerializer(objects, many=True)
#         return Response(serialize.data)

#     def post(self, request):
#         data = request.data
#         datafill = Notification.objects.create(
#             name=data['name'], email=data['email'], )
#         return Response("Successfully Added ")

# class deletedata(GenericAPIView):
#     serializer_class = NotificationSerializer
#     def delete(self, request):
#         data = request.data
#         ourdata = Notification.objects.get(id=data["id"])
#         ourdata.delete()
#         return Response("successfully delte")
