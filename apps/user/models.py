from django.db import models
from django.utils.timezone import now
import hashlib


# from common.validators import mobile_length_validator, mobile_validator, validate_not_empty, email_validator


class User(models.Model):
    """
    This class represents a User of the website
    The variables are self-commented.
    """
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField('gender', max_length=1, choices=[('F', 'female'), ('M', 'male')], blank=True)
    email = models.EmailField(blank=False, unique=True)
    phone_number = models.CharField(max_length=15, blank=True,
                                    )
    password = models.CharField(max_length=10)
    bio = models.TextField(blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    # friends = models.ManyToManyField("User", blank=True, null=True)
    created = models.DateTimeField(default=now)
    active = models.BooleanField(default=False)

    View_profile = models.BooleanField(default=False)

    def __str__(self):
        """
        override __str__()
        :return: user email
        """
        return self.email

    def save(self, *args, **kwargs):
        self.password = hashlib.sha256(self.password.encode('utf-8')).hexdigest()
        super().save(*args, **kwargs)  # Call the "real" save() method.


# class FriendRequest(models.Model):
#     to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.PROTECT)
#     from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.PROTECT)
#     created = models.DateTimeField(auto_now_add=True, blank=True)
#
#     def __str__(self):
#         return "From {}, to {}".format(self.from_user, self.to_user)
#
#     class Meta:
#         ordering = ['-created']

# f=FriendRequest(to_user=User.objects.get(id=3),from_user=User.objects.get(id=4))
# f
# <FriendRequest: From mobinamirzaee74@gmail.com, to malihemirzaee74@gmail.com>
class Following(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follower = models.ManyToManyField(User, related_name="followed")
    followed = models.ManyToManyField(User, related_name="follower")

    @classmethod
    def follow(cls, user, another_account):
        obj, create = cls.objects.get_or_create(user=user)
        obj.followed.add(another_account)
        print("followed")

    @classmethod
    def follow_back(cls, user, another_account):
        obj, create = cls.objects.get_or_create(user=user)
        obj.follower.add(another_account)
        print("followed")

    # @classmethod
    # def unfollow(cls, user, another_account):
    #     obj, create = cls.objects.get_or_create(user=user)
    #     obj.followed.remove(another_account)
    #     print("unfollowed")

    def __str__(self):
        return self.user.email
