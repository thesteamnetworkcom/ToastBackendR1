# Generated by Django 2.2.2 on 2019-07-09 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Complex',
            fields=[
                ('ComplexID', models.CharField(max_length=160, primary_key=True, serialize=False)),
                ('ComplexNo', models.CharField(max_length=150)),
                ('ComplexName', models.CharField(max_length=150)),
                ('InputStatus', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Crosswalk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CMC', models.CharField(max_length=150)),
                ('Lvl2', models.CharField(max_length=150)),
                ('Lvl3', models.CharField(max_length=150)),
                ('Lvl4', models.CharField(max_length=150)),
                ('Lvl5', models.CharField(max_length=150)),
                ('UOM', models.CharField(max_length=150)),
                ('PMTL', models.CharField(max_length=150)),
                ('WorkGroup', models.CharField(max_length=150)),
                ('RSMeans4', models.CharField(max_length=150)),
                ('Lvl5Descr', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('IDNumber', models.CharField(max_length=150)),
                ('Model', models.CharField(max_length=150)),
                ('SerialNum', models.CharField(max_length=150)),
                ('Capacity', models.CharField(max_length=150)),
                ('Manufacturer', models.CharField(max_length=150)),
                ('DateManufactured', models.CharField(max_length=150)),
                ('DateInstalled', models.CharField(max_length=150)),
                ('ControlType', models.CharField(max_length=150)),
                ('WarrantyDate', models.CharField(max_length=150)),
                ('WarrantyConpany', models.CharField(max_length=150)),
                ('WarrantyDate2', models.CharField(max_length=150)),
                ('WarrantyConpany2', models.CharField(max_length=150)),
                ('Location', models.CharField(max_length=150)),
                ('Comment', models.CharField(max_length=150)),
                ('DetailID', models.CharField(max_length=160, primary_key=True, serialize=False)),
                ('LastAnnual', models.CharField(max_length=150)),
                ('InputStatus', models.CharField(max_length=150)),
                ('TestingRequired', models.CharField(max_length=150)),
                ('Rate', models.CharField(max_length=150)),
                ('LastTestDate', models.CharField(max_length=150)),
                ('GroupFlag', models.CharField(max_length=150)),
                ('ComplexID', models.ForeignKey(db_column='ComplexID', on_delete=django.db.models.deletion.CASCADE, to='manage.Complex')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('System', models.CharField(max_length=150)),
                ('Component', models.CharField(max_length=150)),
                ('SectionCategory', models.CharField(max_length=150)),
                ('SectionSubtype', models.CharField(max_length=150)),
                ('SectionName', models.CharField(max_length=150)),
                ('CRV', models.CharField(max_length=150)),
                ('SectionQty', models.CharField(max_length=150)),
                ('SectionUM', models.CharField(max_length=150)),
                ('SectionYear', models.CharField(max_length=150)),
                ('SectionDL', models.CharField(max_length=150)),
                ('SectionAge', models.CharField(max_length=150)),
                ('CSCI', models.CharField(max_length=150)),
                ('CSCCI', models.CharField(max_length=150)),
                ('SectionComment', models.CharField(max_length=150)),
                ('EqpID', models.CharField(max_length=160, primary_key=True, serialize=False)),
                ('CMC', models.CharField(max_length=150)),
                ('PMTL', models.CharField(max_length=150)),
                ('WG', models.CharField(max_length=150)),
                ('LastAnnual', models.CharField(max_length=150)),
                ('InputStatus', models.CharField(max_length=150)),
                ('TestingRequired', models.CharField(max_length=150)),
                ('Rate', models.CharField(max_length=150)),
                ('LastTestDate', models.CharField(max_length=150)),
                ('ComplexID', models.ForeignKey(db_column='ComplexID', on_delete=django.db.models.deletion.CASCADE, to='manage.Complex')),
            ],
        ),
        migrations.CreateModel(
            name='ExcelInfo1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FacilityID', models.CharField(max_length=30)),
                ('EquipmentID', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('FacilityNo', models.CharField(max_length=150)),
                ('RPUID', models.CharField(max_length=150)),
                ('FacilityName', models.CharField(max_length=150)),
                ('RPAType', models.CharField(max_length=150)),
                ('CatCode', models.CharField(max_length=150)),
                ('BldgYear', models.CharField(max_length=150)),
                ('BldgSize', models.CharField(max_length=150)),
                ('BldgStory', models.CharField(max_length=150)),
                ('BldgStatus', models.CharField(max_length=150)),
                ('FacilityID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('InputStatus', models.CharField(max_length=150)),
                ('Zone', models.CharField(max_length=150)),
                ('ComplexID', models.ForeignKey(db_column='ComplexID', on_delete=django.db.models.deletion.CASCADE, to='manage.Complex')),
            ],
        ),
        migrations.CreateModel(
            name='Level2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sect_Name', models.CharField(max_length=150)),
                ('Sect_Description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Level3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sect_Name', models.CharField(max_length=150)),
                ('Sect_Description', models.CharField(max_length=150)),
                ('Level2_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage.Level2')),
            ],
        ),
        migrations.CreateModel(
            name='Level4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sect_Name', models.CharField(max_length=150)),
                ('Sect_Description', models.CharField(max_length=150)),
                ('Level3_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage.Level3')),
            ],
        ),
        migrations.CreateModel(
            name='PMTL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PMTLNumber', models.CharField(max_length=150)),
                ('PMTLDescription', models.CharField(max_length=150)),
                ('Source', models.CharField(max_length=150)),
                ('Daily', models.CharField(max_length=150)),
                ('Weekly', models.CharField(max_length=150)),
                ('Semi_Monthly', models.CharField(max_length=150)),
                ('Monthly', models.CharField(max_length=150)),
                ('Bi_Monthly', models.CharField(max_length=150)),
                ('Quarterly', models.CharField(max_length=150)),
                ('Semi', models.CharField(max_length=150)),
                ('Annual', models.CharField(max_length=150)),
                ('x2Year', models.CharField(max_length=150)),
                ('x3Year', models.CharField(max_length=150)),
                ('x4Year', models.CharField(max_length=150)),
                ('AF120Mo', models.CharField(max_length=150)),
                ('AF221Mo', models.CharField(max_length=150)),
                ('AF340Mo', models.CharField(max_length=150)),
                ('AF45Year', models.CharField(max_length=150)),
                ('AF56Year', models.CharField(max_length=150)),
                ('AF610Year', models.CharField(max_length=150)),
                ('Total', models.CharField(max_length=150)),
                ('Remarks', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FacilityID', models.CharField(max_length=30)),
                ('EquipmentID', models.CharField(max_length=15)),
                ('PMTL', models.CharField(max_length=15)),
                ('Details', models.CharField(max_length=15)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('SiteNo', models.CharField(max_length=150)),
                ('SiteName', models.CharField(max_length=150)),
                ('SiteID', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('InputStatus', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('Passwords', models.CharField(max_length=150)),
                ('Role', models.CharField(max_length=150)),
                ('ActualName', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('User', models.OneToOneField(db_column='USERNAME', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkItem',
            fields=[
                ('SchedDate', models.CharField(max_length=150)),
                ('PMTLNumber', models.CharField(max_length=150)),
                ('WIStatus', models.CharField(max_length=150)),
                ('WIType', models.CharField(max_length=150)),
                ('Qty', models.CharField(max_length=150)),
                ('AssignedBy', models.CharField(max_length=150)),
                ('AssignedDate', models.CharField(max_length=150)),
                ('WorkItemID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('notes', models.CharField(max_length=150)),
                ('Actual', models.CharField(max_length=150)),
                ('AssignedTo', models.ManyToManyField(to='manage.User')),
                ('ComplexID', models.ForeignKey(db_column='ComplexID', on_delete=django.db.models.deletion.CASCADE, to='manage.Complex')),
                ('DetailID', models.ForeignKey(db_column='DetailID', on_delete=django.db.models.deletion.CASCADE, to='manage.Detail')),
                ('EqpID', models.ForeignKey(db_column='EqPID', on_delete=django.db.models.deletion.CASCADE, to='manage.Equipment')),
                ('FacilityID', models.ForeignKey(db_column='FacilityID', on_delete=django.db.models.deletion.CASCADE, to='manage.Facility')),
                ('SiteID', models.ForeignKey(db_column='SiteID', on_delete=django.db.models.deletion.CASCADE, to='manage.Site')),
            ],
        ),
        migrations.CreateModel(
            name='Level5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sect_Name', models.CharField(max_length=150)),
                ('CMC', models.CharField(max_length=150)),
                ('SecNameSec2', models.CharField(max_length=150)),
                ('SecNameSec3', models.CharField(max_length=150)),
                ('Level4_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage.Level4')),
            ],
        ),
        migrations.AddField(
            model_name='facility',
            name='SiteID',
            field=models.ForeignKey(db_column='SiteID', on_delete=django.db.models.deletion.CASCADE, to='manage.Site'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='FacilityID',
            field=models.ForeignKey(db_column='FacilityID', on_delete=django.db.models.deletion.CASCADE, to='manage.Facility'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='SiteID',
            field=models.ForeignKey(db_column='SiteID', on_delete=django.db.models.deletion.CASCADE, to='manage.Site'),
        ),
        migrations.AddField(
            model_name='detail',
            name='EqpID',
            field=models.ForeignKey(db_column='EqPID', on_delete=django.db.models.deletion.CASCADE, to='manage.Equipment'),
        ),
        migrations.AddField(
            model_name='detail',
            name='FacilityID',
            field=models.ForeignKey(db_column='FacilityID', on_delete=django.db.models.deletion.CASCADE, to='manage.Facility'),
        ),
        migrations.AddField(
            model_name='detail',
            name='SiteID',
            field=models.ForeignKey(db_column='SiteID', on_delete=django.db.models.deletion.CASCADE, to='manage.Site'),
        ),
        migrations.AddField(
            model_name='complex',
            name='SiteID',
            field=models.ForeignKey(db_column='SiteID', on_delete=django.db.models.deletion.CASCADE, to='manage.Site'),
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WIID', models.CharField(max_length=150)),
                ('Actual', models.CharField(max_length=150)),
                ('Status', models.CharField(max_length=150)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage.User')),
            ],
        ),
    ]
