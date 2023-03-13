from djoser.serializers import UserCreateSerializer as BaseUserSerializer

class UserCreateSerializer(BaseUserSerializer):
    # here we inherit meta class  of BaseUserSerializer for adding more fields
    class Meta(BaseUserSerializer.Meta):
        fields = ['id','username','email','password','first_name','last_name']
