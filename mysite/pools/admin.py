from django.contrib import admin
from .models import Feedback
from .models import Brand
from .models import Protein
from .models import Gainer
from .models import Creatine
from .models import Bcaa
from .models import Bars

# Register your models here.
admin.site.register(Feedback)
admin.site.register(Brand)
admin.site.register(Protein)
admin.site.register(Gainer)
admin.site.register(Creatine)
admin.site.register(Bcaa)
admin.site.register(Bars)
