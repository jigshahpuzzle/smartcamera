from django.conf.urls import url
from views import test, uploadImage, home

urlpatterns = [
    url(r'^test/', test.as_view(), name='test'),
    url(r'^upload/', uploadImage.as_view(), name='upload'),
    url(r'^$', home.as_view(), name='home'),
]