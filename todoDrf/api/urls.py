from django.urls import path
from .views import (
	apiOverview,
	taskList,
	taskDetail,
	taskCreate,
	taskUpdate,
	taskDelete,

)
app_name='api'

urlpatterns=[
	path('',apiOverview,name='api-overview'),
	path('task-list/',taskList,name='task-list'),
	path('task-create/',taskCreate,name='task-create'),
	path('task-detail/<str:pk>/',taskDetail,name='task-detail'),
	path('task-update/<str:pk>',taskUpdate,name='task-update'),
	path('task-delete/<str:pk>',taskDelete,name='task-delete'),
]