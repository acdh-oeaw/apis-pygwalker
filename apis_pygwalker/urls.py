from django.urls import path
from apis_pygwalker.views import Pygwalker

urlpatterns = [
        path('pygwalker/', Pygwalker.as_view(), name="pygwalker")
        ]
