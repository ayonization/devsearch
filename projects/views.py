from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
# Create your views here.

#This is where the business logic is written


# list of projects (dictionaries)

# projectsList = [
#    {
#       'id': '1',
#       'title': 'Ecommerce Website',
#       'description':'Amazon clone'
#    },
#     {
#       'id': '2',
#       'title': 'Portfolio Website',
#       'description':'Linkedin clone'
#    },
#    {
#        'id':'3',
#        'title': 'Social Network',
#        'description':'Facebook clone'
#    },
# ]

# function to be callled when /projects url is hit
def projects(request):

   #passing page variable as a dictionary to access in template
   # page = 'projects'
   # number = 10
   # context = {'page':page,'number': number,'projectsList':projectsList}


   # return HttpResponse('Here are some responses')

   # all objects from database table of projects
   projects = Project.objects.all()
   context = {'projectsList':projects}

   #renders template projects.html
   return render(request, 'projects/projects.html',context)

# displaying url parameter in response
def project(request,pk):

   # making an object of a project to access and display in templates
   #  projectObj = None  

   #  for i in projectsList:
   #    if i['id'] == pk:
   #       projectObj = i
    #return HttpResponse('Project is '+' '+str(pk))

   # creating an object of project with specific id
   projectObj = Project.objects.get(id=pk)
   
   tags = projectObj.tags.all()
   return render(request,'projects/single-project.html',{'projectObj':projectObj})

# creating new projects using model forms
def createProject(request):

   form = ProjectForm()

   # processing the request when submit button clicked
   if request.method == 'POST':

      # instantiate the form with (post) request data
      # requst.FILES will process image data entered by user
      form = ProjectForm(request.POST,request.FILES)

      # if form is valid, save the data to database and redirect to home page
      if form.is_valid():
         form.save()
         return redirect('projects')

   context = {'form':form}
   return render(request,"projects/project_form.html",context)

# updating projects 
def updateProject(request,pk):

   # project that is to be edited (obtained using id in url)
   project = Project.objects.get(id=pk)

   # create form with feilds filled with data from project obtained above
   form = ProjectForm(instance=project)


   if request.method == 'POST':

      # pass request data (modiefied data for that project) with instance of original project
      # new data from request will be entered into that instance of project
      form = ProjectForm(request.POST,request.FILES,instance=project)

      # save the new form with edited data
      if form.is_valid():
            form.save()
            return redirect('projects')

   context = {'form':form}
   return render(request,"projects/project_form.html",context)

# deleting projects
def deleteProject(request,pk):

   project = Project.objects.get(id = pk)

   if request.method  == 'POST':
      project.delete()
      return redirect('projects')

   context = {'object': project}
   return render(request,'projects/delete-template.html',context)