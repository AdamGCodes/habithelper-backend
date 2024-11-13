from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#Model
from django.contrib.auth import get_user_model, password_validation, hashers
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)
    
    def validate(self, data):
        #Start by removing plain text data from the dictionary that will be sent
        password =data.get('password') #Will be added back after being hashed.
        password_confirmation = data.pop('password_confirmation')#Is obsolete once it's been used to confirm accurate password entry by user.

        #Compare password entries and raise an error if they don't
        if password != password_confirmation:
            raise serializers.ValidationError({ 'password_confirmation': 'Passwords do not match.' })
        
        #If the passwords match, run validators (the ones in project settings and any other you want to add)
        password_validation.validate_password(password)

        #Hash the password and add back to dictionary
        data['password'] = hashers.make_password(password)

        return data


    class Meta:
        # The model we are working with
        model = User
        # Doing a few things but inclues specifying the set of fields we want used in this instance.
        fields = ('id', 'email', 'username', 'password', 'password_confirmation', 'first_name', 'last_name')


# Customise the payload in the JWT It's going to be easier to hve access to the username throughout
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token
