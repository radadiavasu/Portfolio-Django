from django.contrib import admin

# Register your models here.
from content.models import Profile, About, PrimarySkill, SecondarySkill, Service, Portfolio, MyProject, Testomonial, Contact

admin.site.register(Profile)
admin.site.register(About)
admin.site.register(PrimarySkill)
admin.site.register(SecondarySkill)
admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(MyProject)
admin.site.register(Testomonial)
admin.site.register(Contact)