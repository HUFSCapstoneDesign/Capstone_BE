from rest_framework import serializers

from templates.models import Introduce, Template, TemplateCategory


class TemplateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduce
        fields = ["main_image_src"]


class TemplateSerializer(serializers.ModelSerializer):
    introduce = TemplateImageSerializer()

    class Meta:
        model = Template
        fields = "__all__"


class TemplateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateCategory
        fields = "__all__"
