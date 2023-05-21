from rest_framework import serializers

from templates.models import Introduce, Template


class TemplateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduce
        fields = ["main_image_src"]


class TemplateSerializer(serializers.ModelSerializer):
    introduce = TemplateImageSerializer()

    class Meta:
        model = Template
        fields = "__all__"
