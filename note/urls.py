from django.urls import path

from note.views import ShowMainPage, ShowSucces

app_name = 'note'

urlpatterns = [
    path('', ShowMainPage.as_view(), name='main'),
    path('succes', ShowSucces.as_view(), name='succes'),
]
