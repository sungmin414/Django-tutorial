import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .models import Post


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
    # return render(request,'blog/post_list.html')

    # result = ''
    # for post in Post.objects.all():
    #     result += f'-{post}<br/>'
    # return HttpResponse(result)
    # # Post instance에서 title속성에 접근가능
    # # HttpResponse에
    # #
    # # 글 목록
    # # - 격전 참여시..
    # # - 부정행위..
    # # - PBE
    # #
    # # 위 텍스트를 넣어서 리턴
    posts = Post.objects.order_by('-id')
    context = {
        'posts': posts,
    }
    # render는 주어진 인수를 사용해서
    # 1번째 인수 : HttpRequest  인스턴스
    # 2번째 인수 : 문자열 (TEMPLATE['DIRS']를 기준으로 탐색할 템플릿 파일의 경로)
    # 3번째 인수 : 템플릿을 렌더링할때 사용할 객체 모음
    # return render(request, 'blog/post_list.html', context)
    return render(request=request,
                  template_name='blog/post_list.html',
                  context=context,
                  )


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post' : post,
    }
    # post_detail view function이 올바르게 동작하는 html을 작성해서 결과 보기

    return render(request, 'blog/post_detail.html', context)



def post_create(request):
    if request.method == 'POST':
        # request의 method값이 'POST'일 경우 (POST method로 요청이 왔을 경우)
        # request.POST에 있는 title, text값과
        # request.user에 있는 User인스턴스(로그인한 유저)속성을 사용해서
        # 새 Post인스턴스를 생성
        # HttpResponse를 사용해 새로 생성된 인스턴스의 id, title, text정보를 출력 (string)
        post = Post.objects.create(
            author = request.user,
            title = request.POST['title'],
            text = request.POST['text'],
        )
        # Htt Redirection을 보낼 URL
        # http://localhost:8000
        # / 로 시작하면 절대경로, 절대경로의 시작은 도메인 (http://localhost:8000)

        return redirect('post-list')
    else:
        return render(request,'blog/post_create.html')


def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('post-list')



def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        # 글을 수정하기
        # 1. 수정할 내용 (title, text)를 가져온다
        # 2. 수정할 Post인스턴스를 명시
        # 3. 해당하는 Post인스턴스의 title, text를 수정해서 DB에 저장
        # 4. post_detail로 이동
        title = request.POST['title']
        text = request.POST['text']



        post.title = title
        post.text = text
        post.save()

        # post-detail에 해당하는 URL을 만들어내려면,
        # (\d+)에 해당하는 부분을 채울 값이 함께 필요
        # return HttpResponseRedirect('/{}/'.format(post_id))
        return redirect('post-detail', post_id)
    # POST방식이면 어차피 위해서 return되므로 else문 생략
    ctx = {
        'post': post,
    }
    return render(request, 'blog/post_edit.html', ctx)
