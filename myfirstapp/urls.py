from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.myfunctioncall,name="index"),
    path('about',views.myfunctionabout,name="about"),
    path('add/<int:a>/<int:b>',views.add,name='add'),
    path('intro/<str:name>/<int:age>',views.intro,name='intro')
]