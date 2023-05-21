from rest_framework import serializers

from templates.models import Introduce, Template, TemplateCategory, TemplateTag


class TemplateIntroduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduce
        fields = ["main_image_src"]


class TemplateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateCategory
        fields = ["name"]


class TemplateSerializer(serializers.ModelSerializer):
    introduce = TemplateIntroduceSerializer()

    class Meta:
        model = Template
        fields = ["name", "introduce"]


class TemplateTagSerializer(serializers.ModelSerializer):
    template = TemplateSerializer()

    class Meta:
        model = TemplateTag
        fields = ["tag_name", "template"]
