# from django.db import models
#
# from apps.user.models import User
#
#
# class PostManager(models.Manager):
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         user = User.objects.get(active=True)
#         self.user_id = user.pk
