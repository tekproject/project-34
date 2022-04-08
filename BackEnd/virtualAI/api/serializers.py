from rest_framework import serializers 
from .models import BookMark, Url, CustomUser
import django.contrib.auth.password_validation as validators
from django.core import exceptions



class CustomUserSerializer(serializers.ModelSerializer):
    '''Serializers for CustomUser'''
    class Meta:
        model = CustomUser
        exclude = ['password']

    def validate(self, data):
         # here data has all the fields which have validated values
         # so we can create a User instance out of it
         user = CustomUser(**data)

         # get the password from the data
         password = data.get('password')

         errors = dict() 
         try:
             # validate the password and catch the exception
             validators.validate_password(password=password, user=CustomUser)

         # the exception raised here is different than serializers.ValidationError
         except exceptions.ValidationError as e:
             errors['password'] = list(e.messages)

         if errors:
             raise serializers.ValidationError(errors)

         return super(CustomUserSerializer, self).validate(data)


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        if instance.check_password(validated_data['password']):
           super().update(instance, validated_data)
           instance.set_password(validated_data['password'])
           instance.save()
           return instance
        raise serializers.ValidationError({'password':"password doesn't match"})



class BookMarkSerializer(serializers.ModelSerializer):
    '''Serializers for Stock'''
    user = serializers.StringRelatedField(many=False)
    url = serializers.StringRelatedField(many=False)
  
    class Meta:
        model = BookMark 
        fields = '__all__'

class CreateBookMarkSerializer(serializers.ModelSerializer):
    '''Serializers for Stock'''
  
    class Meta:
        model = BookMark 
        fields = '__all__'

class UrlSerializer(serializers.ModelSerializer):
    '''Serializers for Customer'''
    class Meta:
        model = Url 
        fields = '__all__'

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('old_password', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

             # get the password from the data
        password = data.get('password')

        errors = dict() 
        try:
             # validate the password and catch the exception
             validators.validate_password(password=password, user=CustomUser)

         # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
             errors['password'] = list(e.messages)

        if errors:
             raise serializers.ValidationError(errors)

        return super(ChangePasswordSerializer, self).validate(data)


    def update(self, instance, validated_data):
        if instance.check_password(validated_data['old_password']):
           instance.set_password(validated_data['password'])
           instance.save()
           return instance
        raise serializers.ValidationError({"old_password": "Old password is not correct"})

