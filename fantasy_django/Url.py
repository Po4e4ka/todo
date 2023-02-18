from django.urls import path, include


class Url:
    def __init__(self):
        self.urlpatterns = []

    def add_routes(self, routes=[], pre_path=None):
        if pre_path is None:
            self.urlpatterns += [path(route[1], route[0], name=self.__route_name(route)) for route in routes]
        else:
            self.urlpatterns += [
                path(pre_path, include([path(route[1], route[0], name=self.__route_name(route)) for route in routes]))]

    def route(self, view, url):
        return view, url

    @staticmethod
    def __route_name(route):
        return route[2] if len(route) == 3 else route[0].__name__
