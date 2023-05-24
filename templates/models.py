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


# 템플릿 테이블
class Template(models.Model):
    name = models.CharField(max_length=255, unique=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, db_column="member_id")
    template_category = models.ForeignKey(TemplateCategory, on_delete=models.CASCADE, db_column="category_id")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# 이미지 테이블
class Image(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()
    cursive = models.FloatField()
    transparency = models.FloatField()
    angle = models.FloatField()
    template = models.ForeignKey(Template, on_delete=models.CASCADE, db_column="template_id")


# 소개 테이블
class Introduce(models.Model):
    main_image_src = models.CharField(max_length=255, default='')
    full_image_src = models.CharField(max_length=255)
    template = models.ForeignKey(Template, on_delete=models.CASCADE, db_column="template_id")


# 템플릿 태그 테이블
class TemplateTag(models.Model):
    tag_name = models.CharField(max_length=100)
    introduce = models.ForeignKey(Introduce, on_delete=models.CASCADE, db_column="introduce_id")

    def __str__(self):
        return self.tag_name


# 텍스트 테이블
class Text(models.Model):
    content = models.TextField()
    size = models.IntegerField()
    pont = models.CharField(max_length=50)
    x = models.FloatField()
    y = models.FloatField()
    angle = models.FloatField()
    text_color = models.CharField(max_length=50)
    back_color = models.CharField(max_length=50)
    cursive = models.FloatField()
    align = models.BooleanField(default=False)
    line = models.CharField(max_length=50)
    textopa = models.FloatField()
    backopa = models.FloatField()
    zindex = models.IntegerField()
    template = models.ForeignKey(Template, on_delete=models.CASCADE, db_column="template_id")
