from django.urls import path
from . import views

app_name = "chat"
urlpatterns = [
    path("chat/",views.chat_dashboard, name="register"),
    # path("login/",views.user_login, name="login"),
    # path("logout/",views.user_logout, name="logout"),
]