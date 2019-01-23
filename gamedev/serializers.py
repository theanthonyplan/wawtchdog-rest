from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Game, Author, Report, ReportComment, Review
# Supports custom user models
User = get_user_model()


class PrivateField(serializers.ReadOnlyField):
    """
    A Serializer Field class that can be used to hide sensitive User data in the JSON output
    """

    def get_attribute(self, instance):
        # Check if we have a user context or an app context (e.g Oauth2 Client Credentials)
        if self.context.get('request').user is not None:
            if instance.id == self.context.get('request').user.id or self.context.get('request').user.is_superuser:
                return super(PrivateField, self).get_attribute(instance)
        return None

# game seralizer
class UserSerializer(serializers.ModelSerializer):
    """
    Serializing all the users
    """
    # email = PrivateField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')


# author seralizer


# report seralizer


# report comment seralizer
class CommentSerializer(serializers.ModelSerializer):
    """
    Serializing all the comments
    """
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'user_name', 'comment', 'submit_date', 'is_public', 'is_removed']



# review seralizer
