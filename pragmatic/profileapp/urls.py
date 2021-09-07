


from profileapp.views import ProfileUpdateView
from django.urls.conf import path
from profileapp.views import ProfileCreateView


app_name='profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update')
]
