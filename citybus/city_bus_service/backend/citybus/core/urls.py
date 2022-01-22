from django.urls import path
from .import views
urlpatterns = [
   path('',views.home),
   path('route_search/',views.pickup),
   path('route_search_destination/',views.destination),
   path('route_details/',views.route_details),
   path('route_name/',views.route_name),
   path('ticket/',views.ticket),
   path('single_ticket/<str:user_id>',views.signle_ticket),
   
   path('check/',views.check),
   path('fileup/',views.FileUpload.as_view()),
   path('apply_half/',views.apply_half),
   path('review_limit/',views.review_limit),
   path('review_all/',views.review_all),
   path('review_post/',views.review_post),
   path('blog/',views.blogview),
   path('blog/<str:id>/',views.blogDetails),

   path('staffInfo/',views.staffInfo),
   path('#/activate/<str:uid>/<str:token>',views.verification)
   # http://127.0.0.1:8000/#/activate/MjE/azampi-179e3fbbf8aa90d8b30005652f03cbdf

]