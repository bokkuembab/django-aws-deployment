from django.db import models


# Create your models here.
class MyModel(models.Model):
    text = models.CharField(max_length=100)    # 텍스트 필드이며, 최대 길이는 100
    image = models.ImageField(upload_to='image')    # 이미지필드이며, image 폴더에 적용됨
