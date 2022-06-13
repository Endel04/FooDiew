from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from bookmark.models import Bookmark
from accounts.models import Profile


class BookmarkListView(ListView):
    model = Bookmark
    #bookmark_list.html, {'bookmark_list': Bookmark.objects.all()}

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:  # 로그인 하면 사용자의 북마크만 보여주기
            # user -> profile -> bookmark_list
            profile = Profile.objects.get(user=user)  # user-> profile
            bookmark_list = Bookmark.objects.filter(profile=profile)  # profile -> bookmark_list
        else:  # 로그인 안 하면 북마크 보여주지 않기
            bookmark_list = Bookmark.objects.none()
        return bookmark_list


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['profile', 'name', 'url']  #'__all__'
    template_name_suffix = '_create'    #bookmark_from.html -> bookmark_create.html
    success_url = reverse_lazy('bookmark:list')

    def get_initial(self):
        # user -> profile
        user = self.request.user
        profile = Profile.objects.get(user=user)
        return {'profile': profile}


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['name', 'url']  # '__all__'
    template_name_suffix = '_update'  # bookmark_update.html
    # success_url = reverse_lazy('bookmark:list')
    # success_url이 없으면 model의 get_absolute_url() 호출


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')