
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Assignment
from .models import Complex
from .models import Crosswalk
from .models import Detail
from .models import Equipment
from .models import Facility
from .models import Level2
from .models import Level3
from .models import Level4
from .models import Level5
from .models import PMTL
from .models import Site
from .models import User
from .models import WorkItem
from .models import Detail
from .models import Facility
from .models import Shop
from .models import ExcelInfo1
# Register your models here.
admin.site.register(Shop)
@admin.register(ExcelInfo1)
class ExcelInfo1Admin(ImportExportModelAdmin):
    pass

##Distro Database
admin.site.register(Assignment)
@admin.register(Complex)
class ComplexResource(ImportExportModelAdmin):
    pass
@admin.register(Crosswalk)
class CrosswalkResource(ImportExportModelAdmin):
    pass

@admin.register(Detail)
class DataResource(ImportExportModelAdmin):
    pass
@admin.register(Equipment)
class EquipmentResource(ImportExportModelAdmin):
    pass
@admin.register(Facility)
class FacilityResource(ImportExportModelAdmin):
    pass
@admin.register(Level2)
class level2Resource(ImportExportModelAdmin):
    pass
@admin.register(Level3)
class Level3Resource(ImportExportModelAdmin):
    pass
@admin.register(Level4)
class Level4Resource(ImportExportModelAdmin):
    pass
@admin.register(Level5)
class Level5Resource(ImportExportModelAdmin):
    pass
@admin.register(PMTL)
class PMTLResource(ImportExportModelAdmin):
    pass
admin.site.register(Site)
admin.site.register([User])
admin.site.register(WorkItem)
