from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import get_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login

from post_service.forms import LoginForm
from post_service.models import Post


def post_list(request):
    '''
    컨텍스트는 이런식으로 넘긴다!
    :param request:
    :return:
    '''

    template = get_template('post_list.html')

    page_data = Paginator(Post.objects.all(), 3)
    page = request.GET.get('page')

    if page is None:
        page = 1

    try:
        posts = page_data.page(page)
    except PageNotAnInteger:
        posts = page_data.page(1)
    except EmptyPage:
        posts = page_data.page(page_data.num_pages)

    # context는 dict이외의 인스턴스를 필요로 하지 않는다!
    context = {
        'post_list': posts,
        'current_page': page,
        'total_page': range(1, page_data.num_pages + 1)
    }

    return HttpResponse(template.render(context))


def login_page(request):
    template = get_template('login_form.html')

    context = {'login_form': LoginForm()}

    return HttpResponse(template.render(context, request))
    # return render(request, template, context)


def login_validate(request):
    login_form_data = LoginForm(request.POST)

    if login_form_data.is_valid():
        username = login_form_data.cleaned_data['user_id']
        password = login_form_data.cleaned_data['user_password']

        # request를 같이 넣어줘야하냐?
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect('/board/')

        else:
            return HttpResponse('pw or account error.')
    else:
        return HttpResponse('abnormal login form...')

    return HttpResponse('unknown error.')