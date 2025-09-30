from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password):
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)

        return user


class User(PermissionsMixin, AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()


