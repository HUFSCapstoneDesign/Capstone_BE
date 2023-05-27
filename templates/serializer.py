from rest_framework import serializers

from templates.models import Introduce, Template, TemplateCategory, TemplateTag, Image, Text


class TemplateIntroduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduce
        fields = ["main_image_src", "full_image_src"]


class TemplateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateCategory
        fields = ["name"]


class TemplateSerializer(serializers.ModelSerializer):
    introduce = TemplateIntroduceSerializer()
    category = TemplateCategorySerializer()

    class Meta:
        model = Template
        fields = ["id", "name", "introduce", "category"]


class TemplateTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateTag
        fields = ["tag_name"]


class TemplateSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ["width", "height"]


class TemplateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class TemplateTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = "__all__"


class TemplateEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ["width", "height"]
