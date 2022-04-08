from django.db import models
from PIL import Image
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed
    
    # Override the save method of the model
    def save(self):
        super().save()

        img = Image.open(self.image.path) # Open image
        
        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image
            
class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    picture= CloudinaryField('picture')
    projecturl= models.URLField(max_length=200)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    posted= models.DateField(auto_now_add=True )

    def save_posts(self):
        self.user

    def delete_posts(self):
        self.delete()    


    @classmethod
    def search_projects(cls, name):
        return cls.objects.filter(title__icontains=name).all()