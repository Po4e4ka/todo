from apps.custom_auth import views
from fantasy_django.Url import Url

url = Url()
url.add_routes([
    url.route(view=views.auth, url='auth/')
])

urlpatterns = url.urlpatterns
