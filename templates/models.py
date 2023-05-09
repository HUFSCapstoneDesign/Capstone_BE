from django.db import models


# 회원 테이블
class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ": [ 이메일 : " + self.email + " ]"


# 템플릿 테이블 유형
class Template_type(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)


# 템플릿 테이블
class Template(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, db_column="member_id", null=False)
    type = models.ForeignKey(Template_type, on_delete=models.CASCADE, db_column="template_type_id")
    created_at = models.TimeField(auto_now_add=True)
    update_at = models.TimeField(auto_now=True)

    def __str__(self):
        return self.member.name + " 의 템플릿 입니다."


# 이미지 테이블
class Image(models.Model):
    left = models.FloatField(default=0.0, blank=True)
    top = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)
    width = models.FloatField(default=0.0)
    curvature = models.FloatField(default=0.0)
    transparency = models.FloatField(default=0.0)
    angle = models.FloatField(default=0.0)
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
    size = models.IntegerField(default=0)
    pont = models.CharField(max_length=50)
    left = models.FloatField(default=0.0, blank=True)
    top = models.FloatField(default=0.0)
    angle = models.FloatField(default=0.0)
    text_color = models.CharField(max_length=50)
    background_color = models.CharField(max_length=50)
    transparency = models.FloatField(default=0.0)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
