from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.core.urlresolvers import reverse


class Activity(models.Model):
    # activity_id = models.ForeignKey(UserActivity, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=4096)

    def __str__(self):
        return self.name


# make link to activities in user using ManyToManyField
# link: https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.ManyToManyField
# link: https://docs.djangoproject.com/en/1.11/topics/db/queries/
# django 'how to query ManyToManyField
class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    date_of_birth = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=1, default='')
    address_street = models.CharField(max_length=100, default='')
    address_city = models.CharField(max_length=100, default='')
    address_zip = models.CharField(max_length=100, default='')
    address_state = models.CharField(max_length=100, default='')
    address_country = models.CharField(max_length=100, default='')
    height = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    weight = models.DecimalField(max_digits=6, decimal_places=1, default=0)
    bio = models.CharField(max_length=4096, default='')
    image_url = models.CharField(max_length=1000,
                                 default="https://www.1plusx.com/app/mu-plugins/all-in-one-seo-pack-pro/images"
                                         "/default-user-image.png")
    image = models.ImageField(upload_to='profile_image',blank=True)
    activities = models.ManyToManyField(Activity)
    goal = models.CharField(max_length=100, default='')

    # Calculate the Users Age
    def user_age(self):
        import datetime
        dob = self.date_of_birth
        today = datetime.date.today()
        my_age = (today.year - dob.year) - int((today.month, today.day) < (dob.month, dob.day))
        return my_age

    def get_absolute_url(self):
        return reverse('app:profile')

    def __str__(self):
        return self.user.username

# Function to create the users profile when a Django user is created.
# links the Django User to the Profile model
# @receiver(post_save, sender=User)
def create_user_profile(sender, **kwargs):
    if kwargs['created']:  # if User(Django's user) object has been created
        # Create the User's Profile with the current User object
        UserProfile.objects.create(user=kwargs['instance'])

# Connect to the post_save signal, Django's User is the sender here
post_save.connect(create_user_profile, sender=User)


# User Matches Model: create a many to many relationship
# Allows many users to have many users
class UserMatch(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='match_list_owner', null=True)

    @classmethod
    def match_user(cls, current_user, new_match):
        match, created = cls.objects.get_or_create(current_user=current_user)

        match.users.add(new_match)  # Connect current user(match) with the new_match

    @classmethod
    def remove_match(cls, current_user, matched_user):
        match, created = cls.objects.get_or_create(current_user=current_user)

        match.users.remove(matched_user)  # Remove user match from users matches

    def __str__(self):
        return 'matches for ' + self.current_user.username


class MatchSetting(models.Model):
    distance = models.IntegerField()
    gender = models.CharField(max_length=1)
    age_min = models.IntegerField()
    age_max = models.IntegerField()


class Post(models.Model):
    text = models.CharField(max_length=1000)
    timestamp = models.DateField()


class PostComment(models.Model):
    text = models.CharField(max_length=1000)
    timestamp = models.DateField()


class Message(models.Model):
    text = models.CharField(max_length=1000)
    timestamp = models.DateField()
