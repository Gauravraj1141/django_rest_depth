from drf_yasg import openapi

# Swagger Descriptions start here
HEADER_PARAMS = {
    'access_token': openapi.Parameter('accesstoken', openapi.IN_HEADER, description="local header param", type=openapi.IN_HEADER),
}

SAMPLE_INPUT = {
    "authentication_params": {
        "user_profile_id": "34svsdfe3-4036-403d-bf84-cf8400f67836",
        "refresh_token": ""
    },
    "payload": {
        "type_id": "1"
    }
}

SAMPLE_RESPONSE_SUCCESS = {
    "tokens": {
        "new_access_token": ""
    },
    "payload": {
        "faq_questions": {
            "faq_id": "34svsdfe3-4036-403d-bf84-cf8400f67836",
            "faq_question": "What is Aggrement Signing?",
            "faq_type": "1",
            "faq_status": "1",
            "faq_answer": "aggrement signing is a process that will be done property owner and tenant",
            "added_by": "34svsdfe3-4036-403d-bf84-cf8400f67836",
            "added_date": "22 jan 2022",
            "last_modifed_by": "34svsdfe3-4036-403d-bf84-cf8400f67836",
            "last_modified_date": "22 jan 2022",
        }
    }
}


OPERATIONS_DESCRIPTION = """ 
This function will add new property listing details and return the added listing details.
**endpoint url:** baseurl/post_login/property_listing/add_or_update_listing/
"""

INPUT_PROPERTIES_DESCRIPTION = {
"authentication_params": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description="required authentication params for faq",
        example={
            "user_profile_id": "34svsdfe3-4036-403d-bf84-cf8400f67836",
            "refresh_token": ""
        },
        properties={
            "user_profile_id": openapi.Schema(type=openapi.TYPE_STRING,
                                              description='user_profile_id for which property details need to be fetched',
                                              example='34svsdfe3-4036-403d-bf84-cf8400f67836'),
            "refresh_token": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="refresh token",
                example=""),
        }
    ),

"payload": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description="required payload for getting faq question by type",
        example={
            "type_id": "1"
        },
        properties={
            "type_id": openapi.Schema(type=openapi.TYPE_STRING,
                                              description='type_id for which faq questions need to be fetched',
                                              example='1')
        }
    )
}

REQUIRED_LIST = ['authentication_params', 'payload']

RESPONSE_DESCRIPTION = {
    '200': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description='Output if API successfully fetched',
        properties={
            "Status": openapi.Schema(type=openapi.TYPE_STRING, description="Status code of API output", example=200),
            "Message": openapi.Schema(type=openapi.TYPE_STRING, description="Description of API output status",
                                      example="Faq Questions is fetched successfully with "
                                              "service_request_id as80e25939-fce2-11ec-9365-70a6cc340b6f"),
            "Payload": openapi.Schema(
                type=openapi.TYPE_OBJECT, description="Actual fetched information",
                properties={
                    "faq_questions": openapi.Schema(type=openapi.TYPE_OBJECT,
                                                          description="faq questions for selected type",
                                                          example=SAMPLE_RESPONSE_SUCCESS[
                                                              'payload']['faq_questions'],
                                                          properties={
                                                              "faq_id": openapi.Schema(
                                                                  type=openapi.TYPE_STRING,
                                                                  description="faq_id",
                                                                  example="24svsdfe3-5425-403d-bf84-cf8400f67836"
                                                              ),
                                                              "faq_question":  openapi.Schema(
                                                                  type=openapi.TYPE_STRING,
                                                                  description='faq question',
                                                                  example="What is Aggrement Signing?"
                                                              ),
                                                              "faq_type":  openapi.Schema(type=openapi.TYPE_STRING,
                                                                                                      description='faq type for which faq questions fetched to be done',
                                                                                                      example='1'),
                                                              "faq_status": openapi.Schema(type=openapi.TYPE_STRING,
                                                                                                description="faq status type",
                                                                                                example="1"),
                                                              "faq_answer": openapi.Schema(
                                                                  type=openapi.TYPE_STRING,
                                                                  description="Faq Answer",
                                                                  example="aggrement signing is a process that will be done property owner and tenant"
                                                              ),
                                                              "added_by": openapi.Schema(
                                                                  type=openapi.TYPE_STRING,
                                                                  description="Added By ",
                                                                  example="34svsdfe3-4036-403d-bf84-cf8400f67836"
                                                              ),
                                                              "added_date": openapi.Schema(
                                                                  type=openapi.TYPE_STRING,
                                                                  description="added_date",
                                                                  example="22jan 2022"
                                                              ),
                                                              "last_modifed_by": openapi.Schema(
                                                                  type=openapi.TYPE_STRING,
                                                                  description="last_modifed_by",
                                                                  example="34svsdfe3-4036-403d-bf84-cf8400f67836"
                                                              ),
                                                              "last_modified_date": openapi.Schema(
                                                                  type=openapi.TYPE_STRING,
                                                                  description="last_modified_date",
                                                                  example="22 jan 2022"
                                                              ),
                                                          }
                                                          )
                })
        }
    ),
    '404':  openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description='Output if API successfully fetched profile details',
        properties={
            "Status": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Status code of API output",
                example=404),
            "Message": openapi.Schema(type=openapi.TYPE_STRING,
                                      description="Description of status of API output",
                                      example="update_user_profile service"
                                              "with service_request_id ascfc1f659-fce2-11ec-b81b-70a6cc340b6f, "
                                              "could not be executed as given profile_id does not exist in database"
                                      ),
            "Payload": openapi.Schema(
                type=openapi.TYPE_OBJECT, description="The payload will always be an empty dictionary",
                properties={},
                example={}
            )
        }
    ),
    '452':  openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description='Validation failure output',
        properties={
            "Status": openapi.Schema(type=openapi.TYPE_STRING, description="Status code of API output", example=452),
            "Message": openapi.Schema(type=openapi.TYPE_STRING, description="Description of API output status",
                                      example="'user_profile' is a required property")
        }
    )
}

API_LOGIC = """ 
Step 1:
Step 2:
Step 3:
....

"""
# ################ Swagger Descriptions End here  #####################