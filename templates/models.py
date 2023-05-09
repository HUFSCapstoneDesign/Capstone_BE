from django.db import models


# 회원 테이블
class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ": [ 이메일 : " + self.email + " ]"


# 템플릿 테이블 유형
class Template_type(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)


# 템플릿 테이블
class Template(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, db_column="member_id", null=False)
    type = models.ForeignKey(Template_type, on_delete=models.CASCADE, db_column="template_type_id")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# 이미지 테이블
class Image(models.Model):
    left = models.FloatField()
    top = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()
    curvature = models.FloatField()
    transparency = models.FloatField()
    angle = models.FloatField()
    template = models.ForeignKey(Template, on_delete=models.CASCADE)


# 소개 테이블
class Introduce(models.Model):
    src = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    src_type = models.CharField(max_length=20)
    introduce = models.TextField
    template = models.ForeignKey(Template, on_delete=models.CASCADE)


# 텍스트 테이블
class Text(models.Model):
    text = models.TextField()
    size = models.IntegerField()
    pont = models.CharField(max_length=50)
    left = models.FloatField()
    top = models.FloatField()
    angle = models.FloatField()
    text_color = models.CharField(max_length=50)
    background_color = models.CharField(max_length=50)
    transparency = models.FloatField()
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
