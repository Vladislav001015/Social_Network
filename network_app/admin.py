from django.contrib import admin

from network_app.models import Post, Like, DisLike

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(DisLike)
