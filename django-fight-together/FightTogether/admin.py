from django.contrib import admin
from .models import Blog
from .models import Love
from .models import Politics
from .models import Incident
from .models import Refute
from .models import Profile

admin.site.register(Blog)
admin.site.register(Love)
admin.site.register(Politics)
admin.site.register(Incident)
admin.site.register(Refute)
admin.site.register(Profile)