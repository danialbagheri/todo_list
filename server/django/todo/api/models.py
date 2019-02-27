from django.db import models  
from django.contrib.auth.models import User, Group
import os
import random

class Todo(models.Model):
    requested_by = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
    project_number = models.CharField(max_length=200, default='', blank=True)
    position_number = models.EmailField(max_length=500, default='', blank=True)
    status = models.BigIntegerField(default=0, blank=True)
    department = models.ForeignKey(Group, on_delete=models.CASCADE)
    project_detail = models.TextField(blank=True)
#   attached_file = models.ForeignKey(TodoFiles, on_delete=models.CASCADE)
    required_date = models.DateTimeField(auto_now_add=False, blank=True)
    completion_date = models.DateTimeField(auto_now_add=False, blank=True)
    meeting = models.BooleanField(default=False)
    approve = models.BooleanField(default=False)
    amendment = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.project_number

class amendments(models.Model):
    pass

class Comments(models.Model):
    related_todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    comments = models.TextField(Blank=True)
    comment_date = models.DateTimeField(auto_now_add=True,blank=False)

class TodoFiles(models.Model):
    '''
    This model holds all attached files
    '''

    def image_directory_path(self, filename):
        extension = os.path.splitext(filename)[1]
        random_id = random.randint(100, 120)
        new_file_name = "{}-{}-{}-{}-type-{}-{}-id{}{}".format(
            self.product.product_code, self.product.product_category.name, self.product.option_name, self.product.option_value, self.image_type, self.image_angle, random_id, extension)
        # file will upload to media root "product_images/bandName/product_code/Image_type/fileName"
        return "attached-files/{0}/{1}/{2}/{3}".format(self.product.product_category.brand.name, self.product.product_code, self.image_format, new_file_name)

    todo = models.ForeignKey('TODO', on_delete=models.CASCADE)
    file = models.FileField(upload_to=image_directory_path)



    def __str__(self):
        return "{} - {}".format(self.product.product_category.brand.name, self.product)