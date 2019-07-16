from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Shop(models.Model):
    FacilityID = models.CharField(max_length=30)
    EquipmentID = models.CharField(max_length=15)
    PMTL = models.CharField(max_length=15)
    Details= models.CharField(max_length=15)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.FacilityID
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class ExcelInfo1(models.Model):
    FacilityID=models.CharField(max_length=30)
    EquipmentID=models.CharField(max_length=30)


##Site
class Site(models.Model):
    SiteNo = models.CharField(max_length=150)
    SiteName = models.CharField(max_length=150)
    SiteID = models.CharField(max_length=200, primary_key=True)
    InputStatus = models.CharField(max_length=150)
##Complex TABLE
class Complex(models.Model):
    ComplexID = models.CharField( max_length=160, primary_key=True)
    ComplexNo = models.CharField(max_length=150)
    ComplexName = models.CharField(max_length=150)
    SiteID = models.ForeignKey(Site,db_column='SiteID', on_delete=models.CASCADE)
    InputStatus = models.CharField(max_length=150)
##Facility TABLE
class Facility(models.Model):
    FacilityNo = models.CharField(max_length=150)
    RPUID = models.CharField(max_length=150)
    FacilityName = models.CharField(max_length=150)
    RPAType = models.CharField(max_length=150)
    CatCode= models.CharField(max_length=150)
    BldgYear = models.CharField(max_length=150)
    BldgSize = models.CharField(max_length=150)
    BldgStory = models.CharField(max_length=150)
    BldgStatus = models.CharField(max_length=150)
    FacilityID = models.CharField(max_length=150, primary_key=True)
    ComplexID = models.ForeignKey(Complex, db_column='ComplexID', on_delete=models.CASCADE)
    SiteID = models.ForeignKey(Site, db_column='SiteID', on_delete=models.CASCADE)
    InputStatus = models.CharField(max_length=150)
    Zone = models.CharField(max_length=150)
##Equipment TABLE
class Equipment(models.Model):
    System = models.CharField(max_length=150)
    Component = models.CharField(max_length=150)
    SectionCategory = models.CharField(max_length=150)
    SectionSubtype = models.CharField(max_length=150)
    SectionName= models.CharField(max_length=150)
    CRV = models.CharField(max_length=150)
    SectionQty = models.CharField(max_length=150)
    SectionUM = models.CharField(max_length=150)
    SectionYear= models.CharField(max_length=150)
    SectionDL = models.CharField(max_length=150)
    SectionAge = models.CharField(max_length=150)
    CSCI = models.CharField(max_length=150)
    CSCCI= models.CharField(max_length=150)
    SectionComment = models.CharField(max_length=150)
    EqpID =  models.CharField(max_length=160, primary_key=True)
    CMC = models.CharField( max_length=150)
    PMTL = models.CharField(max_length=150)
    WG = models.CharField(max_length=150)
    LastAnnual= models.CharField(max_length=150)
    FacilityID = models.ForeignKey(Facility, db_column='FacilityID', on_delete=models.CASCADE)
    ComplexID = models.ForeignKey(Complex, db_column='ComplexID', on_delete=models.CASCADE)
    SiteID = models.ForeignKey(Site, db_column='SiteID', on_delete=models.CASCADE)
    InputStatus= models.CharField(max_length=150)
    TestingRequired = models.CharField(max_length=150)
    Rate = models.CharField(max_length=150)
    LastTestDate= models.CharField(max_length=150)
##Details TABLE
class Detail(models.Model):
    IDNumber = models.CharField(max_length=150)
    Model = models.CharField(max_length=150)
    SerialNum = models.CharField(max_length=150)
    Capacity = models.CharField(max_length=150)
    Manufacturer = models.CharField(max_length=150)
    DateManufactured= models.CharField(max_length=150)
    DateInstalled= models.CharField(max_length=150)
    ControlType = models.CharField(max_length=150)
    WarrantyDate = models.CharField(max_length=150)
    WarrantyConpany = models.CharField(max_length=150)
    WarrantyDate2 = models.CharField(max_length=150)
    WarrantyConpany2 = models.CharField(max_length=150)
    Location = models.CharField(max_length=150)
    Comment = models.CharField(max_length=150)
    DetailID = models.CharField(max_length=160, primary_key=True)
    LastAnnual = models.CharField(max_length=150)
    EqpID = models.ForeignKey(Equipment, db_column='EqPID', on_delete=models.CASCADE)
    FacilityID = models.ForeignKey(Facility, db_column='FacilityID', on_delete=models.CASCADE)
    ComplexID = models.ForeignKey(Complex, db_column='ComplexID', on_delete=models.CASCADE)
    SiteID = models.ForeignKey(Site, db_column='SiteID', on_delete=models.CASCADE)
    InputStatus = models.CharField(max_length=150)
    TestingRequired= models.CharField(max_length=150)
    Rate = models.CharField(max_length=150)
    LastTestDate = models.CharField(max_length=150)
    GroupFlag = models.CharField(max_length=150)
##WorkItem
class WorkItem(models.Model):
    SiteID = models.ForeignKey(Site,db_column='SiteID', on_delete=models.CASCADE)
    ComplexID = models.ForeignKey(Complex, db_column='ComplexID', on_delete=models.CASCADE)
    FacilityID = models.ForeignKey(Facility, db_column='FacilityID', on_delete=models.CASCADE)
    EqpID = models.ForeignKey(Equipment, db_column='EqPID', on_delete=models.CASCADE)
    DetailID = models.ForeignKey(Detail, db_column='DetailID', on_delete=models.CASCADE)
    SchedDate = models.CharField(max_length=150)
    PMTLNumber = models.CharField(max_length=150)
    WIStatus = models.CharField(max_length=150)
    WIType = models.CharField(max_length=150)
    Qty = models.CharField(max_length=150)
    AssignedTo = models.ManyToManyField('User')
    AssignedBy = models.CharField(max_length=150)
    AssignedDate = models.CharField(max_length=150)
    WorkItemID = models.CharField(max_length=150, primary_key=True)
    notes = models.CharField(max_length=150)
    Actual = models.CharField(max_length=150)
##User
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class User(models.Model):
    User = models.OneToOneField(User,db_column='USERNAME',  on_delete=models.CASCADE)
    Passwords = models.CharField(max_length=150)
    Role = models.CharField(max_length=150)
    ActualName = models.CharField(max_length=150, primary_key=True)
@receiver(post_save,sender=User)
def create_user_profile(sender, created, **kwargs):
    if created:
        User.objects.get_or_create(User=created)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.User.save()


##Assignmets TABLE
class Assignment(models.Model):
    WIID = models.CharField(max_length=150)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Actual = models.CharField(max_length=150)
    Status = models.CharField(max_length=150)
##PMTL TABLE
class PMTL(models.Model):
    PMTLNumber =  models.CharField(max_length=150)
    PMTLDescription = models.CharField(max_length=150)
    Source = models.CharField(max_length=150)
    Daily = models.CharField(max_length=150)
    Weekly = models.CharField(max_length=150)
    Semi_Monthly = models.CharField(max_length=150)
    Monthly = models.CharField(max_length=150)
    Bi_Monthly = models.CharField(max_length=150)
    Quarterly = models.CharField(max_length=150)
    Semi = models.CharField(max_length=150)
    Annual = models.CharField(max_length=150)
    x2Year = models.CharField(max_length=150)
    x3Year = models.CharField(max_length=150)
    x4Year = models.CharField(max_length=150)
    AF120Mo = models.CharField(max_length=150)
    AF221Mo = models.CharField(max_length=150)
    AF340Mo = models.CharField(max_length=150)
    AF45Year = models.CharField(max_length=150)
    AF56Year = models.CharField(max_length=150)
    AF610Year = models.CharField(max_length=150)
    Total = models.CharField(max_length=150)
    Remarks = models.CharField(max_length=150)

##Crosswalk TABLE
class Crosswalk(models.Model):
    CMC = models.CharField(max_length=150)
    Lvl2 = models.CharField(max_length=150)
    Lvl3 = models.CharField(max_length=150)
    Lvl4 = models.CharField(max_length=150)
    Lvl5 = models.CharField(max_length=150)
    UOM= models.CharField(max_length=150)
    PMTL = models.CharField(max_length=150)
    WorkGroup = models.CharField(max_length=150)
    RSMeans4 = models.CharField(max_length=150)
    Lvl5Descr = models.CharField(max_length=150)
##Level2
class Level2(models.Model):
    Sect_Name = models.CharField(max_length=150)
    Sect_Description = models.CharField(max_length=150)
##Level3
class Level3(models.Model):
    Sect_Name = models.CharField(max_length=150)
    Sect_Description = models.CharField(max_length=150)
    Level2_ID = models.ForeignKey(Level2, on_delete=models.CASCADE)
##Level4
class Level4(models.Model):
    Sect_Name = models.CharField(max_length=150)
    Sect_Description = models.CharField(max_length=150)
    Level3_ID = models.ForeignKey(Level3, on_delete=models.CASCADE)
##Level5
class Level5(models.Model):
    Sect_Name = models.CharField(max_length=150)
    CMC = models.CharField(max_length=150)
    Level4_ID = models.ForeignKey(Level4, on_delete=models.CASCADE)
    SecNameSec2 = models.CharField(max_length=150)
    SecNameSec3 = models.CharField(max_length=150)
