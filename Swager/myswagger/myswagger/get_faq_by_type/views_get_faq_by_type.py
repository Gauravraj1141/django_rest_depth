# Core libraries
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response

# Swagger
from drf_yasg.utils import swagger_auto_schema
# from utilities.sessionauthenticators.api.user_session_authenticator.user_session_authenticator import authenticate_pre_login_api_call

# Mandatory
# from utilities.sessionauthenticators.api.user_session_authenticator.user_session_authenticator import \
    # authenticate_post_login_api_call
from .documentation_get_faq_by_type 
from .validations_get_faq_by_type import validations_get_faq_by_type_schema
from utilities.lib import serializer_save, serializer_save_multiple
from apilayer.customersupport.serializers import ContactFormSerializer


# Logging
import logging

logger_info = logging.getLogger('info_logs')
logger_error = logging.getLogger('error_logs')

# API Specific


# @permission_classes([AllowAny])
class AddContactForm(APIView):

    @swagger_auto_schema(
        tags=["Customer Support APIs"],
        # manual_parameters=[HEADER_PARAMS['access_token']],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=REQUIRED_LIST,
            properties=INPUT_PROPERTIES_DESCRIPTION),
        operation_description=OPERATIONS_DESCRIPTION,
        responses=RESPONSE_DESCRIPTION
        )

    # @aws_secrets_authentication
    @authenticate_pre_login_api_call
    @validations_add_contact_form_schema
    def post(self, request):
        """
        :param request:
        :return:
        """ 
        input_json = request.data
        # print(input_json)
        # ######################################################
        # Update Service Name below
        # ######################################################
        input_json['service_name'] = "add_contact_form"
        # ######################################################
        # Update Service Name above
        # ######################################################
        input_json['service_request_id'] = uuid.uuid1()
        logger_info.info(f"{input_json['service_name']} Post function called "
                         f"with service_request_id as {input_json['service_request_id']}")
        json_params = input_json
        output_json = views_add_contact_form_json(json_params)
        return Response(output_json)


def views_add_contact_form_json(request):
    input_json, output_json = request, []
    service_name = input_json['service_name']
    service_request_id = input_json['service_request_id']
    service_function_name = "views_add_contact_form_json"
    try:
        logger_info.info(f"{service_name} service initiated. service request id = {service_request_id}, service_function_name={service_function_name}")
        # ######################################################
        # Write API Logic here
        # ######################################################
       
        contact_form_params = dict(zip(['user_first_name','user_last_name','user_email','user_phone_code','user_contact_number','query_message'],
                               [input_json['payload']['user_first_name'],
                               input_json['payload']['user_last_name'],
                               input_json['payload']['user_email'],
                               input_json['payload']['user_phone_code'],
                               input_json['payload']['user_contact_number'],
                               input_json['payload']['query_message']]))
        
        contact_save_var = serializer_save(ContactFormSerializer,contact_form_params)
        contact_form_params = contact_save_var.data
        output_payload =  contact_form_params
        # output_payload = dict(zip(['token','payload'],[{"new_access_token":input_json['access_token']},contact_form_params]))
        # ##############################################################################################
        # Write API logic above
        # ##############################################################################################

        logger_info.info(f"{service_name} service completed. service request id = {service_request_id}")
        return output_payload

    except Exception as ex:
        logger_error.error(f"Exception Encountered {service_name} service call with "
                           f"service_request_id as {service_request_id} service_function_name={service_function_name}. Exception is : {ex}")
        output_json = dict(zip(['Status', 'Message', 'Request_details', 'Payload'],
                               [500, f"Exception Encountered {service_name} service call with "
                                     f"service_request_id as {service_request_id} service_function_name={service_function_name}. Exception is : {ex}", None, None]))
        return output_json

    
