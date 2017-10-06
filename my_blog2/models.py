from datetime import datetime

from django.db import models

# Create your models here.

class BlogCategory(models.Model):
    name = models.CharField(max_length=20, verbose_name='类别')

    class Meta:
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BlogArticle(models.Model):
    category = models.ForeignKey(BlogCategory, verbose_name='类别', null=True, default='')
    tag = models.CharField(max_length=16, verbose_name='标签')
    title = models.CharField(max_length=80, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    author = models.CharField(max_length=14, default='Judge', verbose_name='作者')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')


    class Meta:
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    blog = models.ForeignKey(BlogArticle, verbose_name='博客文章', null=True)
    name = models.CharField(verbose_name='内容', max_length=20)
    content = models.CharField(verbose_name='内容', max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '博客评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class LeaveMessage(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=20)
    email = models.EmailField(verbose_name='邮箱')
    subject = models.CharField(verbose_name='问题', max_length=50)
    message = models.CharField(verbose_name='信息', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '留言信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name