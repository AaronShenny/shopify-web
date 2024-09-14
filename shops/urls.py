from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'shops'

urlpatterns = [
    # path('',  views.shop),
    path('',views.index,name='index'),
    path('create/',views.CreateProduct, name='create'),
    path('edit/<int:id>/',views.EditProduct, name='edit'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete')
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
