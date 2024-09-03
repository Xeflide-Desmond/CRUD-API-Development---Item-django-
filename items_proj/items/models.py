from django.db import models
from django.contrib.auth.models import User

#Item model
class Item(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    description = models.TextField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    last_modified_by = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.name