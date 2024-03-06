from django.db import models

from pizza_lisa.models import User

class MessagesModel (models.Model):
    user_page = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    author_message = models.CharField(max_length=100, default='admin')
    message = models.TextField()
    date_create = models.DateTimeField(auto_now_add = True)
    new = models.BooleanField (default = True)
    
    def __str__(self):
        return self.message