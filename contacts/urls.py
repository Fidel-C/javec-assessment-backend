from django.urls import path
from contacts import views






urlpatterns = [
    
    path('',views.get_contactS),
    path('',views.post_contact),
    path('<int:pk>/',views.get_contact),
    path('<int:pk>/',views.update_contact),
    path('<int:pk>/',views.delete_contact),
    
]
