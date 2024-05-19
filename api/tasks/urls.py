from django.urls import path

from rest_framework import routers

from tasks import views

app_name = 'tasks'

router = routers.DefaultRouter()
router.register(r'', views.TaskViewSet)

urlpatterns = router.urls
