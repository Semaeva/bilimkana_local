from rest_framework import serializers
from .models import *

from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField


class NewsSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=News)
    news_images = serializers.StringRelatedField(many=True)
    image = serializers.ImageField(
        max_length=None, use_url=True
    )

    class Meta:
        model = News
        fields = "__all__"


class PartnersSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = "__all__"


class ManagersSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Managers)

    class Meta:
        model = Managers
        fields = "__all__"


class TeachersSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Teachers)

    class Meta:
        model = Teachers
        fields = "__all__"


class ProjectsSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Projects)

    class Meta:
        model = Projects
        fields = "__all__"


class ContactsSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Contact)

    class Meta:
        model = Contact
        fields = "__all__"


class CallBackserializer(serializers.ModelSerializer):
    class Meta:
        model = CallBack
        fields = "__all__"


