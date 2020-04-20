from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    url(r'^api/v1/search/', include('search.urls')),
    url(r'^api/v1/passport/', include('authentication.urls'))
]

urlpatterns += static(settings.MEDIA_URL,)
urlpatterns += staticfiles_urlpatterns()
