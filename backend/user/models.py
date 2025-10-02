from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create(self, email, password, **kwargs):
        user = self.model(
            email=self.normalize_email(email),
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_admin", True)

        return self.create(email, password, **kwargs)


class User(PermissionsMixin, AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(blank=True, default=0)
    weight = models.PositiveIntegerField(blank=True, default=0) # kg
    height = models.PositiveIntegerField(blank=True, default=0) # cm  
    personal_records = models.JSONField(default=dict, blank=True)
    personal_goals = models.JSONField(default=dict, blank=True)

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

