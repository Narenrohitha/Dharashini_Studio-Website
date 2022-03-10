from django.contrib import admin
from blog.models import post

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
	('Title/Date',{'fields':['title','date',]}),
	('Content',{'fields':['des','body']})
	]
# Register your models here.
admin.site.register(post,PostAdmin)