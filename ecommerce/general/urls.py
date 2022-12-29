from django.urls import path

from general.views import (
    HomeView,
    # SignupView,
    # LoginView,
)

urlpatterns = [
    path('', HomeView.as_view()),
    # path('signup/', SignupView.as_view()),
    # path('login/', LoginView.as_view()),
]