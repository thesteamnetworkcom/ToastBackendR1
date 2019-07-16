from django.shortcuts import render
from django.http import Http404
# Create your views here.
from django.http import HttpResponse
from .models import Shop
from django.template import loader
from tablib import Dataset
from .resources import ComplexResource

def index(request):
    latest_FacilityID=Shop.objects.order_by('-pub_date')[:5]
    template = loader.get_template('manage/index.html')
    context = {'latest_FacilityID': latest_FacilityID},
    return render(request, 'manage/index.html', context)
def detail(request,FacilityID):
    try:
        FacilityID=Shop.objects.get(pk=FacilityID)
    except FacilityID.DoesNotExist:
        raise Http404('Facility Does not exist')
    return render(request, 'manage/detail.html',{'FacilityID:'})
##ExcelInfo1
def export(request):
    excelInfo1_resource = ExcelInfo1Resource()
    dataset = excelInfo1_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="excel1s.xls"'
    return response
def simple_upload(request):
    if request.method == 'POST':
        excelInfo1_resource = ExcelInfo1Resource()
        dataset = Dataset()
        new_excelInfo1 = request.FILES['myfile']
        imported_data = dataset.load(new_ExcelInfo1.read())
        result = excelInfo1_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            excelInfo1_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'core/simple_upload.html')
##Assignment
def index(request):
    latest_ID=Assignment.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_ID': latest_ID},
    return render(request, 'manage/index.html', context)
def detail(request,ID):
    try:
        ID=Shop.objects.get(pk=ID)
    except ID.DoesNotExist:
        raise Http404('ID Does not exist')
    return render(request, 'manage/detail.html',{'ID:'})
##Complex
##TEST EXPORT/IMPRT
def export(request):
    Complex_resource = ComplexResource()
    dataset = Complex_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="excel1s.xls"'
    return response
def simple_upload(request):
    if request.method == 'POST':
        Complex_resource = ComplexResource()
        dataset = Dataset()
        new_Complex = request.FILES['myfile']
        imported_data = dataset.load(new_Complex.read())
        result = Complex_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            Complex_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'core/simple_upload.html')

##Crosswalk
def export(request):
    Crosswalk_resource = CrosswalkResource()
    dataset = Crosswalk_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="excel1s.xls"'
    return response
def simple_upload(request):
    if request.method == 'POST':
        Crosswalk_resource = CrosswalkResource()
        dataset = Dataset()
        new_Crosswalk = request.FILES['myfile']
        imported_data = dataset.load(new_Crosswalk.read())
        result = Crosswalk_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            Crosswalk_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'core/simple_upload.html')
##Equipment
def export(request):
    Equipment_resource = EquipmentResource()
    dataset = Equipment_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="excel1s.xls"'
    return response
def simple_upload(request):
    if request.method == 'POST':
        Equipment_resource = EquipmentResource()
        dataset = Dataset()
        new_Equipment = request.FILES['myfile']
        imported_data = dataset.load(new_Equipment.read())
        result = Equipment_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            Equipment_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'core/simple_upload.html')
##Facility
def export(request):
    Facility_resource = FacilityResource()
    dataset = Facility_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="excel1s.xls"'
    return response
def simple_upload(request):
    if request.method == 'POST':
        Facility_resource = FacilityResource()
        dataset = Dataset()
        new_Facility = request.FILES['myfile']
        imported_data = dataset.load(new_Facility.read())
        result = Facility_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            Facility_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'core/simple_upload.html')
##Level2
def export(request):
    Level2_resource = Level2Resource()
    dataset = Level2_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="excel1s.xls"'
    return response
def simple_upload(request):
    if request.method == 'POST':
        Level2_resource = Level2Resource()
        dataset = Dataset()
        new_Level2 = request.FILES['myfile']
        imported_data = dataset.load(new_Level3.read())
        result = Level2_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            Level2_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'manage/simple_upload.html')
##Level3
def export(request):
    Level3_resource = Level3Resource()
    dataset = Level3_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="excel1s.xls"'
    return response
def simple_upload(request):
    if request.method == 'POST':
        Level3_resource = Level3Resource()
        dataset = Dataset()
        new_Level3 = request.FILES['myfile']
        imported_data = dataset.load(new_Level3.read())
        result = Level3_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            Level3_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'manage/simple_upload.html')
##Level4
def export(request):
    Level4_resource = Level4Resource()
    dataset = Level4_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="excel1s.xls"'
    return response
def simple_upload(request):
    if request.method == 'POST':
        Level4_resource = Level4Resource()
        dataset = Dataset()
        new_Level4 = request.FILES['myfile']
        imported_data = dataset.load(new_Level4.read())
        result = Level4_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            Level4_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'core/simple_upload.html')
##Level5
def export(request):
    Level5_resource = Level5Resource()
    dataset = Level5_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="excel1s.xls"'
    return response
def simple_upload(request):
    if request.method == 'POST':
        Level5_resource = Level4Resource()
        dataset = Dataset()
        new_Level5 = request.FILES['myfile']
        imported_data = dataset.load(new_Level5.read())
        result = Level5_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            Level5_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'core/simple_upload.html')
##PMTL
def export(request):
    PMTL_resource = PMTLResource()
    dataset = PMTL_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="excel1s.xls"'
    return response
def simple_upload(request):
    if request.method == 'POST':
        PMTL_resource = PMTLResource()
        dataset = Dataset()
        new_PMTL = request.FILES['myfile']
        imported_data = dataset.load(new_PMTL.read())
        result = PMTL_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            PMTL_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'core/simple_upload.html')
##Site
def index(request):
    latest_ID=Site.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_ID': latest_ID},
    return render(request, 'manage/index.html', context)
def detail(request,ID):
    try:
        ID=Shop.objects.get(pk=ID)
    except ID.DoesNotExist:
        raise Http404('ID Does not exist')
    return render(request, 'manage/detail.html',{'ID:'})
##Users
def update_User(request,user_id):
    user=User.objects.get(pk=user_id)
    user.save()
##WorkItem
def index(request):
    latest_ID=WorkItem.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_ID': latest_ID},
    return render(request, 'manage/index.html', context)
def detail(request,ID):
    try:
        ID=Shop.objects.get(pk=ID)
    except ID.DoesNotExist:
        raise Http404('ID Does not exist')
    return render(request, 'manage/detail.html',{'ID:'})

#Details#
def export(request):
    Details_resource = DetailsResource()
    dataset = Details_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="excel1s.xls"'
    return response
def simple_upload(request):
    if request.method == 'POST':
        Details_resource = DetailsResource()
        dataset = Dataset()
        new_Details = request.FILES['myfile']
        imported_data = dataset.load(new_Details.read())
        result = Details_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            Details_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'core/simple_upload.html')
