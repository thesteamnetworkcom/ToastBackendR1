
from import_export import resources
from .models import Assignment
from .models import Complex
from .models import Crosswalk
from .models import PMTL
from .models import Detail
from .models import Equipment
from .models import Facility

class ComplexResource(resources.ModelResource):
    class Meta:
        model = Complex
class CrosswalkResource(resources.ModelResource):
    class Meta:
        model = Crosswalk
class PMTLResource(resources.ModelResource):
    class Meta:
        model = PMTL
        import_id_fields=('ComplexID',)
class DetailResource(resources.ModelResource):
    class Meta:
        model = Detail
class Equipmentresource(resources.ModelResource):
    class Meta:
        model = Equipment
class FacilityResource(resources.ModelResource):
        model = Facility
