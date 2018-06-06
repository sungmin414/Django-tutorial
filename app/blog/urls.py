from django.conf.urls import url

from .views import post_list

urlpatterns = [
    # url의 첫 번째 인자: 매치될 URL정규표현식
    # url의 두 번째 인자: view function
    # view function
    #   -> request를 받아서 response를 돌려주는 함

    url(r'^$', post_list),
]