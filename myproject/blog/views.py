from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import Post
from django.contrib.auth import get_user_model
from django.utils.datastructures import MultiValueDictKeyError



# Create your views here.

def post_list(request) : # helloworld view는 request를 인자로 받아서 HttpPesponse를 돌려줌. 그 내용은 hello world1라는 문자열이다.
    #posts = post.objects.all()
    posts = Post.objects.filter(published_data__isnull=False)
    #.order_by('-created_date') #r 수정
    context = {
        'posts' : posts,
    }
    return render(request, 'blog/post_list.html', context) # render 함수는 두 개의 인자를 필수적으로 받음.
                                        # 첫 번째 인자는 request, 두 번째 인자로는 출력할 템플릿 파일을 받음. 세 번째 인자에 데이터들이 들어있는 딕셔너리 자료형을 받음.

def post_detail(request, pk) :

    post = Post.objects.get(pk=pk)

    # post = Post.objects.first() # 글 하나에 대한 데이터가 필요하므로, .first()메소드를 이용하여 첫 번째 Post 객체 하나를 post변수에 할당
    # POST로 전송되는 데이터는 POST라는 객체로 전달되는데,
    # 이 객체는 QueryDict라는 딕셔너리 타입의 데이터임.
    # 이 데이터에 접근하려면 request.POST로 입력하면 됨.
    context = {
        'post' : post
    }
    return render(request, 'blog/post_detail.html', context)

def post_add(request) :
    if request.method == 'POST' :
        # author 필드에 넣을 User 객체를 불러올 때
        User = get_user_model()
        # User 객체를 통해 이름이 'gyu'인 User객체를 불러와 'author' 변수에 할당.
        author = User.objects.get(username='gyu')
        # POST요청으로 받아온 POST 딕셔너리 데이터의 키를 호출하여 변수에 할당.
        title = request.POST['title']
        content = request.POST['content']

        '''
        ORM을 통해서 Post 객체를 생성하고, 생성한 Post 객체의 title, content 필드에
        POST 데이터로부터 가져온 데이터를 할당한 변수들을 넣어줌.
        생성된 Post객체를 post라는 변수에 할당하여, Post모델의 인스턴스를 만들어 줌.
        하지만 Post객체는 반드시 작성자를 뜻하는 author 필드를 채워주어야 함.
        그리고 이 author 필드는 User 테이블과 연결된 외래키 필드이므로, User 객체로만 채워질 수 있음.
        '''

        post = Post.objects.create(
            author = author,
            title = title,
            content = content,
        )
        # publish 메서드 호출.
        # published_data 필드가 비어있으면 메인 화면에서 글이 보이지 않으므로, 처리.
        # post는 Post객체이므로, 미리 만들어두었던 publish 메서드를 활용

        post.publish()
        post_pk = post.pk

        # redirect() 함수는 인자로 다음의 세 가지를 받을 수 있음.
        # 모델 : 모델의 get_absolute_url() 함수가 실행되어 그 결과가 인자로 전달됨
        # 뷰 : 뷰가 인자를 받는다면, redirect('뷰이름, 매개변수명 = 인자)의 형태로 뷰에 인자를 전달해줄 수 있음.
        return redirect(post_detail, pk=post_pk)
        # 주의! : 뷰 오브젝트 자체를 넘겨주어도 작동하지만, 그렇게 할 경우 역참조 url문제가 발새할 수 있어, 권장되지 않음.
        # 절대 또는 상대 URL 주소 : 해당 주소로 요청을 보냄.
        # 우리의 경우, 등록한 글의 pk(기본키)를 post_pk 변수에 할당하고,
        # 이것을 post_detail 뷰에 전달한 것을 redirect 함수의 인자로 전달하였음.


    elif request.method == 'GET' :
        return render(request, 'blog/post_add.html')

def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()
        return render(request, 'blog/post_delete.html')

    elif request.method == 'GET':
        return HttpResponse('잘못된 접근 입니다.')


