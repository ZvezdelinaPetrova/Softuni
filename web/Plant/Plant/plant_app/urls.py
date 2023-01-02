from django.urls import path

from Plant.plant_app.views import index, edit_plant, details_plant, delete_plant, \
    details_profile, add_plant, create_profile, delete_profile, edit_profile, catalog_page

urlpatterns = (
    path('', index, name='show index'),

    path('catalogue/', catalog_page, name='show catalog'),

    path('create/', add_plant, name='create plant'),
    path('edit/<int:pk>', edit_plant, name='edit plant'),
    path('details/<int:pk>', details_plant, name='details plant'),
    path('delete/<int:pk>', delete_plant, name='delete plant'),

    path('profile/create/', create_profile, name='create profile'),
    path('profile/details/', details_profile, name='details profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)

