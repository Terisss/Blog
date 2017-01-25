"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from article.views import index, article, category, create_comments, del_comments, update_comment,logout, RegistrationForm, LoginForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^([0-9]+)/$', index, name="page"),
    url(r'^article/([0-9]+)/$', article, name='article'),
    url(r'^category/([0-9]+)/$', category, name='category'),
    url(r'^category/(?P<category_id>[0-9]+)/(?P<num>[0-9]+)/$', category, name='category_page'),
    url(r'^comments/([0-9]+)/$', create_comments, name="create_comments"),
    url(r'^comments/([0-9]+)/delete$', del_comments, name='del_comments'),
    url(r'^comments/([0-9]+)/update$', update_comment, name='update_comment'),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', logout, name='logout'),
    url(r'^reg/$', RegistrationForm.as_view(), name='reg'),
    url(r'^login/$', LoginForm.as_view(), name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
