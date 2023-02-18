from apps.todo import views
from fantasy_django.Url import Url

url = Url()
# ------------ todo group
url.add_routes(
    pre_path='todo/',
    routes=[
        url.route(views.todo, url=''),
        url.route(views.add_new_todo, 'add/'),
        url.route(views.delete_todo, '<int:todo_id>/delete/'),
        url.route(views.clear_completed, 'clear_completed/'),
        url.route(views.change_status, '<int:todo_id>/change_status/')
    ])

urlpatterns = url.urlpatterns
