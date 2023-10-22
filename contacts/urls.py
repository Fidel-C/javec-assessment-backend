from django.urls import path
from contacts import views






urlpatterns = [
    
    path('',views.get_contactS),
    path('<int:pk>',views.get_contact),
    path('<int:pk>/update/',views.update_contact),
    path('<int:pk>/delete/',views.delete_contact),
    
]
