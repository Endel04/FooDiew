from django import forms
from bookmark.models import Bookmark


class BookmarkCreationForm(forms.ModelForm):
    url = forms.CharField(label='링크', widget=forms.Textarea)

    class Meta:
        model = Bookmark
        fields = ['name', 'url']

    def save(self, commit=True):
        new_bookmark = Bookmark.objects.create(
            name=self.cleaned_data.get('name'),  # 사용자가 입력한 내용을 clean_name() 후 clean한 name 가져오기
            url=self.cleaned_data('url'),  # 사용자가 입력한 내용을 clean_url() 후 clean한 url 가져오기
        )
        return new_bookmark