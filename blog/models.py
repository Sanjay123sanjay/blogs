from django.db import models
from ckeditor.fields import RichTextField
class Category(models.Model):
    class Meta:
        verbose_name_plural='categories'
    title=models.CharField(max_length=20)
    slug = models.CharField(max_length=50, unique=True, null=False)
    def __str__(self):
        return self.title
class Blog(models.Model):
    title=models.CharField(max_length=300)

    content=RichTextField()
    def __str__(self):
        return self.title
    pub_date=models.DateTimeField()

    category=models.ForeignKey(Category,on_delete=models.CASCADE)
class Comment(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.TextField()
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE
                           )
