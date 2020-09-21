from django.urls import path
from .views import index, details, results, final


urlpatterns = [
    path('', index, name='index'),
    path('<int:q_id>/', details, name='detail'),
    path('<int:q_id>/results/', results, name='results'),
    path('<int:q_id>/final/', final, name='final')
]
