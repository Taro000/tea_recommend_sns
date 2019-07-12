from django.contrib import admin
from .models import *


admin.site.register(UserProfile)
admin.site.register(Tea)
admin.site.register(Evaluation)
admin.site.register(Preference)
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Follower)
admin.site.register(Favorite)
