from django.shortcuts import render
from .models import DiaryModel
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

class DiaryList(ListView):
    template_name = 'diaryapp/list.html'
    model = DiaryModel

class DiaryCreate(CreateView):
    template_name = 'diaryapp/create.html'
    model = DiaryModel
    fields = ('date', 'title', 'text')
    success_url = reverse_lazy('list')

class DiaryDetail(DetailView):
    template_name = 'diaryapp/detail.html'
    model = DiaryModel
    