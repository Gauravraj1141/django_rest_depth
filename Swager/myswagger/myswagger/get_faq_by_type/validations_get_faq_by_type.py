import logging
import uuid
from functools import wraps
from rest_framework.views import Response
from pathlib import Path
from utilities.validators.views import schema_validation

logger_info = logging.getLogger('info_logs')
logger_error = logging.getLogger('error_logs')

def validations_get_faq_by_type_schema(func):
    """Function to validate api call fields."""
    @wraps(func)
    def validations_get_faq_by_type_json(self, request):
        """
            :param None:
            :return:
            """

        validation_service_request_id = uuid.uuid1()
        # ######################################################
        # Configure the below piece for validations
        # ######################################################
        validation_service_name = "get_faq_by_type"
        service_app_location = "customersupport"
        schema_location = f"apilayer/{service_app_location}/api/{validation_service_name}"
        p = Path.cwd() / f"{schema_location}/schema_{validation_service_name}.json"
        # ######################################################################################
        # Configure the above piece for validations. No need to change anything below this line
        # ######################################################################################

        try:
            logger_info.info(f"{validation_service_name} validation function initiated with "
                             f"validation_service_request_id as {validation_service_request_id}")
            data = request.data
            # print(data)

            schema_val = schema_validation(data, p)
            if schema_val['Status'] == 452:
                logger_info.info(f"{validation_service_name} validation failed with "
                                 f"validation_service_request_id as {validation_service_request_id}")
                return Response(schema_val)
            else:
                pass

        except Exception as ex:
            logger_info.error(f"Exception encountered in validation for {validation_service_name}  with "
                              f"validation_service_request_id as {validation_service_request_id}. "
                              f"Exception is: {ex}")
            output_json = dict(zip(['Status', 'Message', 'Payload'],
                                   [452, f"Exception encountered in validation for {validation_service_name}  with"
                                         f"validation_service_request_id as {validation_service_request_id}. "
                                         f"Exception is: {ex}", dict()]))
            return Response(output_json)

        logger_info.info(f"{validation_service_name} validation function successfully passed with "
                         f"validation_service_request_id as {validation_service_request_id}")
        return func(self, request)

    return validations_get_faq_by_type_json