from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('main.urls')),
	path('accounts/logout/', 
        	auth_views.LogoutView.as_view(
             		next_page='tasks_list',
             		http_method_names=['get', 'post']  # Разрешаем оба метода
        	), 
         	name='logout'),
	path('accounts/', include('django.contrib.auth.urls')),
]