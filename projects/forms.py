# create model forms here 

from django.forms import ModelForm
from .models import Project

class ProjectForm (ModelForm) :

    class Meta :
        # Model for which form is created
        model = Project
        # Include all the feilds in the above model
        fields = ['title','featured_image','description','demo_link','source_link','tags']