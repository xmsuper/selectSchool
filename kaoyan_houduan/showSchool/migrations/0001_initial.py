# Generated by Django 4.1.5 on 2023-03-28 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('name', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('code', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
                ('feature_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'feature',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hotsearchschool',
            fields=[
                ('school_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'hotsearchschool',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('major_name', models.CharField(max_length=50)),
                ('major_code', models.CharField(max_length=50)),
                ('major_class', models.CharField(max_length=10)),
                ('level1_name', models.CharField(max_length=50)),
                ('level2_name', models.CharField(max_length=50)),
                ('spe_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'major',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'province',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProvinceA',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'province_a',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProvinceB',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'province_b',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProvinceOther',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'province_other',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolImg',
            fields=[
                ('school_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('school_img', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'school_img',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learntype', models.CharField(db_column='learnType', max_length=10)),
                ('major_code', models.CharField(max_length=20)),
                ('major_name', models.TextField()),
                ('total', models.CharField(blank=True, max_length=10, null=True)),
                ('politics', models.TextField(blank=True, null=True)),
                ('english', models.TextField(blank=True, null=True)),
                ('procourse', models.TextField(blank=True, null=True)),
                ('procourese2', models.TextField(blank=True, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('school_name', models.TextField(blank=True, null=True)),
                ('school_tel', models.TextField(blank=True, null=True)),
                ('school_email', models.TextField(blank=True, null=True)),
                ('school_web', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'school_score',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolType',
            fields=[
                ('name', models.CharField(max_length=10, unique=True)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('type_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'school_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('userpassword', models.CharField(db_column='userPassword', max_length=80)),
            ],
            options={
                'db_table': 'userinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolInfo',
            fields=[
                ('is_211', models.IntegerField()),
                ('type_name', models.CharField(blank=True, max_length=50, null=True)),
                ('type_school_name', models.CharField(max_length=50)),
                ('province_area', models.CharField(max_length=10)),
                ('syl', models.IntegerField(blank=True, null=True)),
                ('clicks', models.IntegerField(blank=True, null=True)),
                ('is_985', models.IntegerField(blank=True, null=True)),
                ('is_zihuaxian', models.IntegerField(blank=True, null=True)),
                ('rk_rank', models.IntegerField(blank=True, null=True)),
                ('province_name', models.CharField(blank=True, max_length=20, null=True)),
                ('is_ads', models.IntegerField(blank=True, null=True)),
                ('school_id', models.IntegerField(primary_key=True, serialize=False)),
                ('school_name', models.ForeignKey(db_column='school_name', on_delete=django.db.models.deletion.DO_NOTHING, to='showSchool.schoolimg')),
            ],
            options={
                'db_table': 'school_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SchoolDetail',
            fields=[
                ('belongsto', models.CharField(blank=True, db_column='belongsTo', max_length=50, null=True)),
                ('create_date', models.CharField(blank=True, max_length=50, null=True)),
                ('intro', models.TextField(blank=True, null=True)),
                ('num_doctor', models.IntegerField(blank=True, null=True)),
                ('num_lab', models.IntegerField(blank=True, null=True)),
                ('num_master', models.IntegerField(blank=True, null=True)),
                ('num_subject', models.IntegerField(blank=True, null=True)),
                ('school_space', models.CharField(blank=True, max_length=50, null=True)),
                ('school_name', models.TextField(blank=True, null=True)),
                ('school_address', models.TextField(blank=True, null=True)),
                ('province', models.TextField(blank=True, null=True)),
                ('school_img', models.TextField(blank=True, null=True)),
                ('school_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('zhaoban_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('school_site', models.TextField(blank=True, null=True)),
                ('zhaoban_site', models.TextField(blank=True, null=True)),
                ('school_email', models.TextField(blank=True, null=True)),
                ('school_id', models.IntegerField(primary_key=True, serialize=False)),
                ('school_detail_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='showSchool.schoolinfo')),
            ],
            options={
                'db_table': 'school_detail',
                'managed': True,
            },
        ),
    ]
