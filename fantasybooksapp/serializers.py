from rest_framework import serializers
from .models import Book_Description, Book, CustomUser, Bookmark

class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id','email', 'password')
        extra_kwargs = {'password': {'write_only' : True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)  # We use **validated_data to encrypt the password
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop('password', None)
        return ret
    
class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'book', 'page', 'userId']
        
class BookDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_Description
        fields = ['id', 'title', 'author', 'description', 'type', 'cover', 'bookContent']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'bookTitle', 'content']

