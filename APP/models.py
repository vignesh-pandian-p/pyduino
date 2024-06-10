from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=30, null=False, blank=False)
    password = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField()

class API(models.Model):
    user = models.OneToOneField(Register, on_delete=models.CASCADE)
    apiKey = models.CharField(max_length=30, null=False, blank=False)
    
class Messages(models.Model):
    username=models.CharField(max_length=30, null=False, blank=False)
    message=models.CharField(max_length=100, null=False, blank=False)



from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, name, domain, password=None):
        if not email:
            raise ValueError('The Email field is required')
        if not name:
            raise ValueError('The Name field is required')
        if not domain:
            raise ValueError('The Domain field is required')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, domain=domain)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, domain, password=None):
        user = self.create_user(email, name, domain, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

from django.db import models

class InternshipApplication(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    domain = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullname
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'domain']
    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True


    @property
    
    def is_staff(self):
        return self.is_admin


   
