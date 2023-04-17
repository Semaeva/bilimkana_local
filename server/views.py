from django.shortcuts import render
from .send_mail import send_mail, send_back_call
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from .models import *

# Create your views here.


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class PartnerListView(generics.ListAPIView):
    queryset = OurPartner.objects.all()
    serializer_class = PartnersSerializer


class ManagersListView(generics.ListAPIView):
    queryset = Managers.objects.all()
    serializer_class = ManagersSerializer


class TeachersListView(generics.ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer


class ProjectsListView(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class ContactsListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactsSerializer


class CallBackListView(generics.CreateAPIView):
    queryset = CallBack.objects.all()
    serializer_class = CallBackserializer

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            send_back_call(html=
                           f"<p> ФИО: {request.data['name']} </p>"
                           f"<p>Номер телефона: {request.data['phone']}</p>"
                           f"<p>Возраст студента: {request.data['age']}</p>", school= f"{request.data['school']}",
                           text='test',
                           subject=f"Обратный звонок",
                           from_email='wunata95@gmail.com',
                           to_emails=['wunata95@gmail.com',])
            return self.create(request, *args, **kwargs)
