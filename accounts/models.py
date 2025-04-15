from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
#Model for super-admin
class MyAccountManager(BaseUserManager):
    #user bnane ka tareeka define krti hai
    #to create a normal user
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address.')

        if not username:
            raise ValueError('User must have an username.')

        #creating the user
        user = self.model(
            email=self.normalize_email(email),  #fixes the capital letters in emails
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password) #inbuild function to used for setting the password hashed
        user.save(using=self._db) #User object ko database me save kar, aur wo database use kar jo currently is manager ne choose kiya hai
        return user #issse wo bana hua user object wapas return karte hain taaki jahan pe create_user() call hua hai, wahan se use kiya ja sake


    #using create_user we are making a (super user)
    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password  # Missing password fixed
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


#Abstract base user class (Account Model for normal users)
class Account(AbstractBaseUser):#custom user model hai jisme hum apne fields define karte hain jo user ki details store karte hain
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)  # Fixed max_length
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15)  # Fixed max_length

    #mandiatory when creating a user field always include
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email' #which we need to login with
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']  # Fixed 'user_name' to 'username'

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None): #if user is admin he has all the permission to make changes
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
