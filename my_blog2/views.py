from django.shortcuts import render
from django.views import View

from my_blog2.forms import LeaveMessageForm
from .models import BlogComment, BlogArticle, BlogCategory, LeaveMessage


# Create your views here.


class HomeView(View):
    def get(self, request):
        #获取文章（按时间排序）
        articles = BlogArticle.objects.order_by('-add_time')
        #获取类别
        categorys = BlogCategory.objects.all()[:3]
        #获取最近文章
        recent_posts = BlogArticle.objects.order_by('-add_time')[:3]
        return render(request, 'index.html', {
            'articles':articles,
            'categorys':categorys,
            'recent_posts':recent_posts,
        })


class blogView(View):
    def get(self, request):
        #获取文章（按时间排序）
        articles = BlogArticle.objects.order_by('-add_time')
        return render(request, 'full-width.html', {
            'articles':articles
        })


class AritcleView(View):
    def get(self, request, article_id):
        article = BlogArticle.objects.get(id=article_id)
        # 获取最近文章
        recent_posts = BlogArticle.objects.order_by('-add_time')[:3]
        # 获取类别
        categorys = BlogCategory.objects.all()[:3]
        return render(request, 'single.html', {
            'article':article,
            'recent_posts':recent_posts,
            'categorys':categorys,
        })


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html', {})


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html', {})

    def post(self, request):
        # 使用form判断用户POST输入是否合法
        message_form = LeaveMessageForm(request.POST)
        # 判断输入是否合法，如果合法执行以下逻辑
        if message_form.is_valid():
            message = LeaveMessage()
            message.email = request.POST.get('email', '')
            message.name = request.POST.get('name', '')
            message.subject = request.POST.get('subject', '')
            message.message = request.POST.get('message', '')
            message.save()
            return render(request, 'contact.html', {'msg': '发送成功'})
        else:
            return render(request, 'contact.html', {'message_form': message_form})













