from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.utils.translation import gettext as _

"""Serializers for the user API View"""
"""Serializers is just a way of to convert to and from python objects"""

class UserSerializer(serializers.ModelSerializer):
    """Serializer for user object"""
    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only':True, 'min_length': 6}}

    def create(self, validated_data):
        """method to create and return a user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)
        """ (**) operator gathers all the named arguments and makes a dictionary.
        When calling a function, it takes a dictionary and breaks it into named arguments"""

    def update(self, instance, validated_data):
        """method to update and return a user"""
        password = validated_data.pop('password', None) #pop remove  the password from dict after retrieving
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

class AuthTokenSerializers(serializers.Serializer):
    """Serializers for the user authentication Token"""
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        """this validate and authenticate the user that is login"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(request=self.context.get('request'), username=email, password=password)

        if not user:
            msg = _('Authentication failed')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs