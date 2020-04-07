# class형 뷰의 generic view를 이용하여 구현
# ListView/CreateView/UpdateView/DeleteView/DetailView 구현
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Photo
from django.contrib import messages 

#like 버튼 views 위해 
from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponseForbidden
from urllib.parse import urlparse

#like 함수
class PhotoLike(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated: #로그인 확인 되지 않을 시 
            return HttpResponseForbidden()  #자료 숨기기
        
        else:
            if 'photo_id' in kwargs: #photo_id 확인
                photo_id = kwargs['photo_id']
                photo = Photo.Objects.get(pk=photo_id) #photo는 pk를 가진다
                user = request.user
                if user in photo.like.all():
                    photo.like.remove(user) #user가 이미 좋아요 했다면 클릭해서 좋아요 지워짐
                else:
                    photo.like.add(user) #user가 좋아요하지않았다면, 좋아요에 더한다
            referer_url = request.META.get('HTTP_REFERER') 
            path = urlparse(referer_url).path #메인페이지에 좋아요 누르면 그 페이지에 있게하고
            return HttpResponseRedirect(path) #상세페이지 좋아요를 누르면 그 페이지로 redirect

#favorite 저장 함수
class PhotoFavorite(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:    #로그인확인
            return HttpResponseForbidden()
        else:
            if 'photo_id' in kwargs:
                photo_id = kwargs['photo_id']
                photo = Photo.objects.get(pk=photo_id)
                user = request.user
                if user in photo.favorite.all():
                    photo.favorite.remove(user)
                else:
                    photo.favorite.add(user)
            return HttpResponseRedirect('/')



class PhotoList(ListView):
    model = Photo
    template_name_suffix = '_list'
#PhotoList:가장 메인에서 보여줄 로직 / 모델을 불러와서 데이터를 활용할 것이라고 기제
class PhotoCreate(CreateView):
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_create'
    success_url = '/'


    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            # 올바르지 않다면
            return self.render_to_response({'form': form})

# PhotoCreate:
# 모델을 활용하는데생성할 때 채워야 할 필드 확인이후 연결될 템플릿 이름은 Photo_create 일 것이다.
#성공하면 메인 페이지로 돌아가도록 연결(이후 url로 연결)

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_update'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()

        if object.author != request.user:
            messages.warning(request, '수정할 권한이 없습니다.')

            return HttpResponseRedirect('/')
            #삭제페이지에 권한이 없다고 띄우거나
            #detail 페이지 들어가서 삭제에 실패했다고 띄우거나

        else:
            return super(PhotoUpdate, self).dispatch(request, *args, **kwargs)

#photoUpdate : Create와 동일

class PhotoDelete(DeleteView):
    model = Photo
    template_name_suffix = '_delete'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()

        if object.author != request.user:
            messages.warning(request, '삭제할 권한이 없습니다.')
            return HttpResponseRedirect('/')

        return super(PhotoDelete, self).dispatch(request, *args, **kwargs)

class PhotoDetail(DetailView):
    model = Photo
    template_name_suffix = '_detail'



#PhotoDelete와 PhotoDetail
#삭제와 상세페이지는 특별한 로직이 필요하지 않음
#템플릿과 연결을 잘 시킬 수 있도록
