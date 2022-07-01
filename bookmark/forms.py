from django import forms
from bookmark.models import Bookmark


class BookmarkCreationForm(forms.ModelForm):
    url = forms.CharField(label='링크', widget=forms.Textarea)

    class Meta:
        model = Bookmark
        fields = ['name', 'url']

    def clean_url(self):
        url = self.cleaned_data.get('url')  # url 가져오기
        if not (url.startswith('http://') or url.startswith('https://')):  # http:// or https://가 없으면
            url = 'https://' + url  # https:// 추가하기
        return url

    def save(self, commit=True):
        new_bookmark = Bookmark.objects.create(
            name=self.cleaned_data.get('name'),  # 사용자가 입력한 내용을 clean_name() 후 clean한 name 가져오기
            url=self.cleaned_data.get('url'),  # 사용자가 입력한 내용을 clean_url() 후 clean한 url 가져오기
        )
        return new_bookmark