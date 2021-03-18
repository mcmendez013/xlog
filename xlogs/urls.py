# Defines URL patterns for xlogs

from django.urls import path

from . import views

app_name = 'xlogs'

urlpatterns = [
	#Home Page
	path('',views.index,name='index'),

    #Show all categories
    path('categories/', views.categories, name='categories'),

    #Details page foe single category
    path('categories/<int:category_id>/', views.category, name='category'),

    #Page for adding a new topic
    path('new_cat/', views.new_cat, name='new_cat'),

    #Page for adding a new entry
    path('new_entry/<int:category_id>/', views.new_entry, name='new_entry'),

    #Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),


] 
