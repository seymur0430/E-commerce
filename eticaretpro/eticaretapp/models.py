from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractUser
from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _


class CustomUserManager(UserManager):

    def _create_user_object(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        # GlobalUserModel = apps.get_model(
        #     self.model._meta.app_label, self.model._meta.object_name
        # )
        # username = GlobalUserModel.normalize_username(username)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        return user
    
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        user = self._create_user_object(email, password, **extra_fields)
        user.save(using=self._db)
        return user
    
    async def _acreate_user(self, email, password, **extra_fields):
        """See _create_user()"""
        user = self._create_user_object(email, password, **extra_fields)
        await user.asave(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    create_user.alters_data = True

    async def acreate_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return await self._acreate_user(email, password, **extra_fields)

    acreate_user.alters_data = True

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    create_superuser.alters_data = True

    async def acreate_superuser(
        self, email=None, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return await self._acreate_user(email, password, **extra_fields)

    acreate_superuser.alters_data = True


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    objects = CustomUserManager()
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    



class Banner(models.Model):
    image = models.ImageField(upload_to="banner_images/")
    
    class Meta:
        ordering = ("-id",)
        
    def __str__(self):
        return self.image.url


class Product(models.Model):
    CONDITIONS =(
        ('GOOD', 'GOOD'),
        ('Perfect', 'Perfect'),
        ('Bad', 'Bad')
    )
    TYPES = (
        ('Family', 'Family'),
        ('Kids', 'Kids'),
        ('Office', 'Office')
    )
    name = models.CharField(verbose_name='AD',max_length=100)
    image = models.ImageField(upload_to="product_images/")
    price = models.FloatField(default=0) 
    percentage = models.FloatField(default=0)
    discount_price = models.FloatField(default=0)
    is_stock=models.BooleanField(default=True)
    
    cover_image = models.ImageField(upload_to="product_images/")
    condition = models.CharField(max_length=7, choices=CONDITIONS, default='Good')
    type = models.CharField(max_length=6, choices=TYPES, default='Family')
    
    
    class Meta:
        ordering = ("-id",)
        
    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        discount_price = self.price * self.percentage / 100
        self.discount_price = self.price -discount_price
        return super(Product, self).save(*args, **kwargs)
    
    
    
class ProductContent(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="product_images/")
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="contents")
        
    class Meta:
        ordering = ("-id",)
        
    def __str__(self):
        return self.title
    
    
class ProductPhoto(models.Model):
    image = models.ImageField(upload_to="product_images/")
    
    class Meta:
        ordering = ("-id",)
        
    def __str__(self):
        return self.image.url
    
    
class Review(models.Model):
    name =models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    image = models.ImageField(upload_to="review_imgs/")
    position = models.CharField(max_length=50)
    star = models.FloatField(default=0)
    
    class Meta:
        ordering = ("-id",)
        
    def __str__(self):
        return self.name
    
    
class Contanct(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=256)
    message = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
    
    class Meta:
        ordering = ("-id",)
        
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='site_images/', blank=True, null=True)
    banner_title = models.TextField( blank=True, null=True)
    banner_content =models.TextField( blank=True, null=True)
    
    story_title = models.TextField( blank=True, null=True)
    story_subtitle = models.TextField( blank=True, null=True)
    story_content = models.TextField( blank=True, null=True)
    story_image = models.ImageField(upload_to="site_images/",  blank=True, null=True)
    story_image1 = models.ImageField(upload_to='site_images/',  blank=True, null=True)
    story_image2 = models.ImageField(upload_to='site_images/',  blank=True, null=True)
    
    opening_hours = models.TextField( blank=True, null=True)
    opening_image = models.ImageField(upload_to='site_imahes/',  blank=True, null=True)
    
    short_about = models.TextField( blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=256, blank=True, null=True)
    
    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"
        
    def save(self, *args, **kwargs):
        if not self.id and SiteSettings.objects.exists():
            pass
        return super(SiteSettings,self).save(*args, **kwargs)
        
    def __str__(self):
        return "Settings"
    
    
class Store(models.Model):
    location = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ("-id",)
        
    def __str__(self):
        return self.location
    
from django.utils import timezone
  
class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_wishlistitems")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_wishlistitems")
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ("-id",)
        
    def __str__(self):
        return self.user.username + " | " + self.product.name
    
 
 
  
class Approval(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_approvalitems")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_approvalitems")
    created_at = models.DateTimeField(default=timezone.now)
    
    
    class Meta:
        ordering = ("-id",)
        
    def __str__(self):
        return self.user.username + " | " + self.product.name