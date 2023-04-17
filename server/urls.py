from django.urls import path
from .views import *

urlpatterns = [
    path('news/list/', NewsListView.as_view()),
    path('teachers/list/', TeachersListView.as_view()),
    path('managers/list/', ManagersListView.as_view()),
    path('projects/list/', ProjectsListView.as_view()),
    path('partners/list/', PartnerListView.as_view()),
    path('callback/list/', CallBackListView.as_view()),
    path('contacts/list/', ContactsListView.as_view()),

]