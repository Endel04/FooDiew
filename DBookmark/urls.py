from django.contrib import admin
from django.urls import path, include
from bookmark.views import BookmarkListView

urlpatterns = [
    path('', BookmarkListView.as_view(), name='home'),
    path('bookmark/', include('bookmark.urls')),
    path('admin/', admin.site.urls),
]
