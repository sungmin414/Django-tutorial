import os

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


def post_list(request):

    # cur_file_path = os.path.abspath(__file__)
    # blog_dir = os.path.dirname(cur_file_path)
    # app_dir = os.path.dirname(blog_dir)
    # templates_dir = os.path.join(app_dir,'templates')
    # post_list_template_path = os.path.join(templates_dir, 'blog','post_list.html')
    # html = open(post_list_template_path,'rt').read()

    # 경로에 해당하는 HTML파일을 문자열로 로드해줌
    # html = render_to_string('blog/post_list.html')
    # # 가져온 문자열을 돌려주
    # return HttpResponse(html)

    # 위 명령어 줄여쓴 말
    return render(request,'blog/post_list.html')