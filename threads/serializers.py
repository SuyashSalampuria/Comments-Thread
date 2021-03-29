import datetime

from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Page, ParentMessage, ThreadMessage, ParentMessage


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User Model
    """

    class Meta:
        """
        Meta Class for UserSerializer
        """
        model = User
        fields = ['id', 'username']


class ThreadMessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Thread Message Objects
    """

    user = UserSerializer(read_only=True)
    is_edited = serializers.SerializerMethodField()

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


    class Meta:
        """
        Meta class for ThreadMessageSerializers
        """
        model = ThreadMessage
        exclude = ['datetime_modified', 'datetime_created']

    def get_is_edited(self, message):
        """
        Checks if a message has been edited or not
        """
        return (message.datetime_modified-message.datetime_created).total_seconds() > 0.1


class ParentMessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Parent Message Objects and all its child messages
    """
    user = UserSerializer(read_only=True)
    is_edited = serializers.SerializerMethodField()
    read_only_fields = ['user']
    child_messages = ThreadMessageSerializer(read_only=True, many=True)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        """
        Meta class for ParentMessageSerializers
        """
        model = ParentMessage
        exclude = ['datetime_modified', 'datetime_created']

    def get_is_edited(self, message):
        """
        Checks if a message has been edited or not
        """
        return (message.datetime_modified-message.datetime_created).total_seconds() > 0.1


class ParentOnlyMessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Parent Message Objects
    """
    user = UserSerializer(read_only=True)
    is_edited = serializers.SerializerMethodField()
    read_only_fields = ['user']

    class Meta:
        """
        Meta class for ParentOnlyMessageSerializers
        """
        model = ParentMessage
        exclude = ['datetime_modified', 'datetime_created']

    def get_is_edited(self, message):
        """
        Checks if a message has been edited or not
        """
        return (message.datetime_modified-message.datetime_created).total_seconds() > 0.1


class PageSerializer(serializers.ModelSerializer):
    """
    Serializer for Page Objects and showing all its Parent Messages without any Thread Message
    """
    user = UserSerializer(read_only=True)
    messages = ParentOnlyMessageSerializer(read_only=True, many=True)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        """
        Meta class for PageSerializers
        """
        model = Page
        fields = '__all__'


class PageDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for Page Objects and showing all its Parent Messages without any Thread Message
    """
    user = UserSerializer(read_only=True)
    messages = ParentMessageSerializer(read_only=True, many=True)

    class Meta:
        """
        Meta class for PageDetailSerializers
        """
        model = Page
        fields = '__all__'
