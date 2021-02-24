from django.utils import timezone
from django.utils.timezone import now
from django.db import models
from apps.user.models import User
from math import floor


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(default=now)
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    @property
    def age(self):
        age_year = timezone.now().year - self.created_date.year
        age_month = timezone.now().month - self.created_date.month
        age_day = timezone.now().day - self.created_date.day
        age_hour = timezone.now().hour - self.created_date.hour
        if age_year >= 1:
            return '{} years a go'.format(floor(age_year))
        elif age_month >= 1:
            return '{} months a go'.format(floor(age_month))
        elif age_day >= 1:
            return '{} days a go'.format(floor(age_month))
        elif age_hour > 1:
            return '{} hours a go'.format(floor(age_hour))
        else:
            return 'recently'


class Comment(models.Model):
    note = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=now)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
    user_id = models.OneToOneField('user.User', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.note[:20]


class Like(models.Model):
    created_date = models.DateTimeField(default=now)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.user_id
