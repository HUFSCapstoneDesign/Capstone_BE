from rest_framework import serializers

from templates.models import Introduce, Template, TemplateCategory, TemplateTag, Image, Text


class TemplateIntroduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduce
        fields = ["main_image_src", "full_image_src"]


class TemplateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateCategory
        fields = "__all__"


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


class TemplateSaveSerializer(serializers.ModelSerializer):
    images = TemplateImageSerializer(many=True)
    texts = TemplateTextSerializer(many=True)
    tags = TemplateTagSerializer(many=True)
    introduces = TemplateIntroduceSerializer(many=True)

    class Meta:
        model = Template
        fields = ["name", "category", "introduce", "images", "texts", "tags", "introduces"]

    def create(self, validated_data):
        images_data = validated_data.pop("images")
        texts_data = validated_data.pop("texts")
        tags_data = validated_data.pop("tags")
        introduces_data = validated_data.pop("introduces")

        category = validated_data.pop("category")

        template = Template.objects.create(
            category=category,
            **validated_data
        )

        for image_data in images_data:
            Image.objects.create(template=template, **image_data)

        for text_data in texts_data:
            Text.objects.create(template=template, **text_data)

        for tag_data in tags_data:
            TemplateTag.objects.create(template=template, **tag_data)

        for introduce_data in introduces_data:
            Introduce.objects.create(template=template, **introduce_data)

        return template
