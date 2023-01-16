from django.db import models
import uuid
# Create your models here.

# This is where database tables are created
# Migrating new models turn them into database tables


class Project(models.Model):
     title = models.CharField(max_length=200)
     description = models.TextField(null=True,blank=True) # null values allowed in db, blank submissions allowed
     featured_image = models.ImageField(null=True,blank=True,default= 'default.jpg' )
     demo_link = models.CharField(max_length=2000,null=True,blank=True)
     source_link = models.CharField(max_length=2000,null=True,blank=True)
     # Creating many to many relationships
     tags = models.ManyToManyField('Tag',blank=True)
     vote_total = models.IntegerField(default=0,null=True,blank=True)
     vote_ratio = models.IntegerField(default = 0,null=True,blank = True)
     created = models.DateTimeField(auto_now_add=True)
     id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
     
     # Accessing model in admin panel gives title not object
     def __str__(self):
          return self.title

class Review(models.Model):
     # tuple to allow users only two values in value attribute below
     VOTE_TYPE = {
          ('up','Up Vote'),
          ('down','Down Vote'),
     }
     #owner =
     # Foreign key project whose review is written (One to many)
     # When project is deleted , review will be deleted (cascaded)
     project = models.ForeignKey(Project,on_delete=models.CASCADE)
     body = models.TextField(null=True,blank=True)
     value = models.CharField(max_length=200,choices = VOTE_TYPE) 
     created = models.DateTimeField(auto_now_add=True)
     id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

     def __str__(self):
          return self.value

class Tag(models.Model):
      name = models.CharField(max_length=200)
      created = models.DateTimeField(auto_now_add=True)
      id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

      def __str__(self):
          return self.name