from django.db import models


# 회원 테이블
class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 템플릿 테이블 유형
class TemplateCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# 소개 테이블
class Introduce(models.Model):
    main_image_src = models.CharField(max_length=255, default='')
    full_image_src = models.CharField(max_length=255)


# 템플릿 테이블
class Template(models.Model):
    name = models.CharField(max_length=255, unique=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, db_column="member_id")
    template_category = models.ForeignKey(TemplateCategory, on_delete=models.CASCADE, db_column="category_id")
    introduce = models.ForeignKey(Introduce, on_delete=models.CASCADE, db_column="introduce_id")
    width = models.IntegerField()
    height = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# 이미지 테이블
class Image(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()
    opacity = models.FloatField()
    src = models.CharField(max_length=255)
    radis = models.FloatField()
    border_style = models.TextField()
    zindex = models.IntegerField()
    gray_scale = models.FloatField()
    blur = models.FloatField()
    brightness = models.FloatField()
    contrast = models.FloatField()
    hue = models.FloatField()
    invert = models.FloatField()
    saturate = models.FloatField()
    sepia = models.FloatField()
    border_size = models.FloatField()
    border_color = models.TextField()
    template = models.ForeignKey(Template, on_delete=models.CASCADE, db_column="template_id")


# 템플릿 태그 테이블
class TemplateTag(models.Model):
    tag_name = models.CharField(max_length=100)
    template = models.ForeignKey(Template, on_delete=models.DO_NOTHING, db_column="template_id")

    def __str__(self):
        return self.tag_name


# 텍스트 테이블
class Text(models.Model):
    content = models.TextField()
    size = models.IntegerField()
    font = models.CharField(max_length=50)
    x = models.FloatField()
    y = models.FloatField()
    text_color = models.CharField(max_length=50)
    back_color = models.CharField(max_length=50)
    cursive = models.FloatField()
    align = models.BooleanField(default=False)
    underlined = models.BooleanField(default=False)
    textopa = models.FloatField()
    backopa = models.FloatField()
    zindex = models.IntegerField()
    bold = models.BooleanField(default=False)
    italic = models.BooleanField(default=False)
    template = models.ForeignKey(Template, on_delete=models.CASCADE, db_column="template_id")
