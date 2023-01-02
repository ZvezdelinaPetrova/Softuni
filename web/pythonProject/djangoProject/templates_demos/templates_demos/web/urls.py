from django.urls import path

from templates_demos.web.views import index, redirect_to_home, about

urlpatterns = (
    path('', index, name='index'),
    path('go-to-home/', redirect_to_home, name='redirect to home'),
    path('about/', about, name='about'),
)

'''
Create django app
1. Add to `installed_apps`
2. Create urls.py in the app
3. Include app's urls.py in the project's urs.py
'''