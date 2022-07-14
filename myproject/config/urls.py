from django.contrib import admin
from django.urls import re_path as url

from blog.views import post_list, post_detail, post_add, post_delete
# views.py에서 만든 post_list 함수를 가져옴.



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', post_list), # url 객체를 만들어 줌.
    url(r'^post/(?P<pk>\d+)/$', post_detail), # post로 시작하는 url 주소와 매치
                                        # 정규표현식 post/(?P<pk>\d+)/ : post/ 에 이어서 \d+ 즉, 어떤 숫자 \d가 1개 이상 + 올 수 있으며, 그 숫자는 pk라는 이름의
                                        #그룹에 포함된다는 뜻. pk = primary key의 약자.(기본키)

    url(r'^post/add/$', post_add, name='post_add'),
    url(r'^post/(?P<pk>\d+)/delete/', post_delete, name='post_delete'),


]
