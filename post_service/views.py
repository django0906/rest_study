from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import auth

from post_service.forms import LoginForm
from post_service.models import Post


def post_list(request):
    template = get_template('post_list.html')

    page_data = Paginator(Post.objects.all(), 5)
    page = request.GET.get('page')

    if page is None:
        page = 1

    try:
        posts = page_data.page(page)
    except PageNotAnInteger:
        posts = page_data.page(1)
    except EmptyPage:
        posts = page_data.page(page_data.num_pages)

    context = {'post_list': posts, 'current_page': page, 'total_page': range(1, page_data.num_pages + 1)}

    return HttpResponse(template.render(context))


def login(request):
    template = get_template('login_form.html')

    context = {'login_form': LoginForm()}
    context.update(csrf(request))

    return HttpResponse(template.render(context))


def login_validate(request):
    login_form_data = LoginForm(request.POST)

    if login_form_data.is_valid():
        user = auth.authenticate(
            username=login_form_data.cleaned_data['id'],
            password=login_form_data.cleaned_data['password']
        )
        if user is not None:
            if user.is_active:
                auth.login(request, user)

                redirect('/board')

        else:
            return HttpResponse('사용자 없음 혹은 비밀번호 오류.')
    else:
        return HttpResponse('로그인 폼이 비정상.')

    return HttpResponse('알 수 없는 오류')