from apps.example import views
from fantasy_django.Url import Url

url = Url()
url.add_routes([
    url.route(view=views.main_page, url='')
])

urlpatterns = url.urlpatterns
