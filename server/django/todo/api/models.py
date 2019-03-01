from django.db import models  
from django.contrib.auth.models import User, Group
import os
import random
class Designer(models.Model):
    designer = models.ForeignKey(User, verbose_name="designers", on_delete=models.CASCADE)
    role = models.CharField(max_length=200, default='', blank=True)
    def __str__(self):
        return self.designer.username

class Todo(models.Model):
    requested_by = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
    project_number = models.CharField(max_length=200, default='', blank=True)
    position_number = models.CharField(max_length=10, default='', blank=True)
    status = models.CharField(max_length=200, blank=True)
    project_detail = models.TextField(blank=True)
    requested_date = models.DateTimeField(auto_now_add=True, blank=True)
#   attached_file = models.ForeignKey(TodoFile, on_delete=models.CASCADE)
    required_date = models.DateField(auto_now_add=False, blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    meeting = models.BooleanField(default=False)
    approve = models.BooleanField(default=False)
    amend = models.BooleanField(default=False)
    amendment = models.IntegerField(default=0)
    assigned_to = models.ForeignKey(Designer, on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.project_number

    def clean(self):
        if self.amend:
            self.amendment = self.amendment + 1
            self.amendment.save()

        



class Comment(models.Model):
    related_todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    comment_date = models.DateTimeField(auto_now_add=True,blank=False)

    def __str__(self):
        return self.related_todo.project_number

class TodoFile(models.Model):
    '''
    This model holds all attached files
    '''

    def image_directory_path(self, filename):
        extension = os.path.splitext(filename)[1]
        random_id = random.randint(100, 120)
        new_file_name = "{}-{}.{}".format(
            self.todo.project_number, random_id, extension)        # file will upload to media root "product_images/bandName/product_code/Image_type/fileName"
        return "attached-files/{0}/{1}}".format(self.todo.project_number, new_file_name)

    todo = models.ForeignKey('TODO', on_delete=models.CASCADE)
    file = models.FileField(upload_to=image_directory_path)



    def __str__(self):
        return "{}".format(self.todo.project_number)