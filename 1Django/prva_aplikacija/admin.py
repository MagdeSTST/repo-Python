from django.contrib import admin

from .models import Lice
from .models import Post
from .models import Klient
from .models import Naracka

admin.site.register(Lice)
admin.site.register(Post)
admin.site.register(Klient)
admin.site.register(Naracka)

# Register your models here.
