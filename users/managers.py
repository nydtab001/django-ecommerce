from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a regular user.
        """
        if not email:
            raise ValueError('The Email field must be set')

        # Normalize the email address
        email = self.normalize_email(email)
        # Create a new user instance
        user = self.model(email=email, **extra_fields)
        # Set the password for the user
        user.set_password(password)
        # Save the user object
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)