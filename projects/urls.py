from django.urls import path
from projects.views import project,projects
from . import views

urlpatterns = [
    # when you go to the url(route) /projects, execute projects function
    # empty first parameter means root domain 
    path('',projects,name="projects"),

    #dynamically passing a value in url to be displayed in response
    path('project/<str:pk>',project,name="project"),
    
    path('create-project/',views.createProject,name = "create-project" ),

    # select a project to update, pass id in url
    path('update-project/<str:pk>',views.updateProject,name = "update-project" ),

    path('delete-project/<str:pk>',views.deleteProject,name = "delete-project" )
        
]