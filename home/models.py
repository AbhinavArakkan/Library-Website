from django.db import models

class Member(models.Model):
    position = models.CharField(max_length=100) 
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='member_imgs')
    
    class Meta:
        ordering = ['position']
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
    
    def __str__(self):
        return f"{self.name} - {self.position}"


class Image(models.Model):
    img = models.ImageField(upload_to='imgs')
    # Remove uploaded_date since it doesn't exist in the old table
    
    class Meta:
        db_table = 'home_images'  # Keep using old table
        ordering = ['-id']  # Order by ID instead of uploaded_date
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
    
    def __str__(self):
        return f"Image {self.id}"
    
    

class NewsItem(models.Model):
    headline = models.CharField(max_length=500)
    image = models.ImageField(upload_to='news_images/')
    uploaded_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['-uploaded_date']
        verbose_name = 'News Item'
        verbose_name_plural = 'News Items'

    def __str__(self):
        return self.headline