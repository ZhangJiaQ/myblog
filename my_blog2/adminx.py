from .models import BlogArticle, BlogComment, BlogCategory
import xadmin

class BlogArticleAdmin(object):
    list_display = [ 'tag', 'title', 'content', 'author', 'add_time']
    search_fields = [ 'tag', 'title', 'content', 'author', 'add_time']
    list_filter = ['tag', 'title', 'content', 'author', 'add_time']


class BlogCommentAdmin(object):
    list_display = ['blog', 'name', 'content', 'add_time']
    search_fields = ['blog', 'name', 'content', 'add_time']
    list_filter = ['blog', 'name', 'content', 'add_time']


class BlogCategoryAdmin(object):
    list_display = ['name', ]
    search_fields = ['name', ]
    list_filter = ['name', ]



xadmin.site.register(BlogArticle, BlogArticleAdmin)
xadmin.site.register(BlogComment, BlogCommentAdmin)
xadmin.site.register(BlogCategory, BlogCategoryAdmin)