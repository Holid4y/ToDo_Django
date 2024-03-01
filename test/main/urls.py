from django.urls import path
from .views import index, add_task, delete_task, get_tasks, edit_task, update_task_status

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('add_task/', add_task, name='add_task'),
    path('delete_task/', delete_task, name='delete_task'),
    path('get_tasks/', get_tasks, name='get_tasks'),
    path('edit_task/', edit_task, name='edit_task'),
    path('update_task_status/', update_task_status, name='update_task_status'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
