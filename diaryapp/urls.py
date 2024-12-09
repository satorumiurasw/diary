from django.urls import path
from .views import DiaryList, DiaryCreate, DiaryDetail, DiaryUpdate, DiaryDelete

urlpatterns = [
    path('', DiaryList.as_view(), name='list'),
    path('create/', DiaryCreate.as_view(), name='create'),
    path('detail/<int:pk>', DiaryDetail.as_view(), name='detail'),
    path('update/<int:pk>', DiaryUpdate.as_view(), name='update'),
    path('delete/<int:pk>', DiaryDelete.as_view(), name='delete'),
]
