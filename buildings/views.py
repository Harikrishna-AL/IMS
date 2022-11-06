from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from buildings.models import Building
from django.contrib import admin
def index(request):
    return render(request, 'index.html')

# class ArticleView(ListView):
#     model = Building
#     def get_state_data(self, **kwargs):
#         state = super().get_state_data(**kwargs)
#         state['now'] = timezone.now()
        # return state


class EventAdminSite(admin.AdminSite):
    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        ordering = {
            "Buildings": 1,
            "Blocks": 2,
            "Floors": 3,
            "Rooms": 4,
            "Items": 5,
        }
        app_dict = self._build_app_dict(request)
        # a.sort(key=lambda x: b.index(x[0]))
        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: ordering[x['name']])

        return app_list