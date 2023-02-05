from drf_yasg import openapi


SAMPLE_INPUT = {
    "Create User": {
        "name": "gaurav",
        "email": "rajput@gmail.com"
    }
}

SAMPLE_RESPONSE_SUCCESS = {
    "Payload": {
        "Status": [
            {
                "Created User Successfully"
            }

        ]
    }
}

INPUT_PROPERTIES_DESCRIPTION = {
    "user creadentials": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description="required authentication params for lisitng",
        example={
            "Create User": {
                "name": "gaurav",
                "email": "rajput@gmail.com"
            }
        },
        properties={
            "user_name": openapi.Schema(type=openapi.TYPE_STRING,
                                        description='name',
                                        example='Gaurav Rajput'),

        }
    )
}


REQUIRED_LIST = ["user_name", "email"]

RESPONSE_DESCRIPTION = {
    '200': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description='Output if API successfully fetched  notification',
    )
}
