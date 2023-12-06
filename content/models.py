from django.db import models

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to="profile/")
    fullname = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    bio = models.TextField()
    cv = models.FileField(upload_to="profile/cv/", max_length=100) 

    class Meta:
        verbose_name = ("profile")
        verbose_name_plural = ("profiles")

    def __str__(self):
        return self.fullname
  
    
class About(models.Model):
    long_about = models.TextField()
    short_about = models.TextField()

    class Meta:
        verbose_name = ("About")
        verbose_name_plural = ("Abouts")

    def __str__(self):
        return self.short_about
    
class PrimarySkill(models.Model):
    icon = models.ImageField(upload_to="Primaryskill/")
    name = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = ("PrimarySkill")
        verbose_name_plural = ("PrimarySkills")

    def __str__(self):
        return self.name

class SecondarySkill(models.Model):
    icon = models.ImageField(upload_to="Secondaryskill/")
    name = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = ("SecondarySkill")
        verbose_name_plural = ("SecondarySkills")

    def __str__(self):
        return self.name
    
    
class Service(models.Model):
    link = models.CharField(max_length=150)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("Services")

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    link = models.CharField(max_length=150)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Portfolio")
        verbose_name_plural = ("Portfolios")

    def __str__(self):
        return self.name
    
    
class MyProject(models.Model):
    link = models.CharField(max_length=150)
    heading = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("MyProject")
        verbose_name_plural = ("MyProjects")

    def __str__(self):
        return self.heading

    
class Testomonial(models.Model):
    image = models.ImageField(upload_to="testomonial/client")
    image_name = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    quote = models.TextField()

    class Meta:
        verbose_name = ("Testomonial")
        verbose_name_plural = ("Testomonials")

    def __str__(self):
        return self.fullname


class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.fullname
