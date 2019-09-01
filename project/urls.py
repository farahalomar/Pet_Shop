from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.pet_list, name="pet-list"),
    path('detail/<int:pet_id>/', views.pet_detail, name='pet-detail'),
    path('create/', views.pet_create, name='pet-create'),
    path('update/<int:pet_id>/', views.pet_update, name='pet-update'),
    path('delete/<int:pet_id>/', views.pet_delete, name='pet-delete'),
    path('signup/',views.signup ,name='signup'),
    path('signin/',views.signin ,name='signin'),
    path('signout/',views.signout ,name='signout'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)