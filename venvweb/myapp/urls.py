##예상 라우트 경로 예시##
# http://127.0.0.1/
# http://127.0.0.1/app/
# http://127.0.0.1/create/
# http://127.0.0.1/read/1 
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index), # 경로없이 접속시 views의 index함수 실행
    path('create/', views.create),
    path('read/<id>/', views.read),
     path('delete/', views.delete),
     path('update/<id>/', views.update)

]