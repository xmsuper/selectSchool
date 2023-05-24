# Generated by Django 4.1.5 on 2023-05-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showSchool', '0003_alter_article_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
                ('optionsA', models.TextField()),
                ('optionsB', models.TextField()),
                ('optionsC', models.TextField()),
                ('optionsD', models.TextField()),
                ('answer', models.TextField()),
                ('explation', models.TextField()),
            ],
            options={
                'verbose_name': '题库',
                'db_table': 'zhengzhitiku',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'managed': True, 'verbose_name': '帖子'},
        ),
        migrations.AlterModelOptions(
            name='article_comment',
            options={'managed': True, 'verbose_name': '评论'},
        ),
        migrations.AlterModelOptions(
            name='countryline',
            options={'managed': False, 'verbose_name': '国家线'},
        ),
        migrations.AlterModelOptions(
            name='hotsearchschool',
            options={'managed': False, 'verbose_name': '热搜院校'},
        ),
        migrations.AlterModelOptions(
            name='major',
            options={'managed': False, 'verbose_name': '专业'},
        ),
        migrations.AlterModelOptions(
            name='majordetail',
            options={'managed': False, 'verbose_name': '专业详情'},
        ),
        migrations.AlterModelOptions(
            name='schooldetail',
            options={'managed': True, 'verbose_name': '学校详情'},
        ),
        migrations.AlterModelOptions(
            name='schoolimg',
            options={'managed': False, 'verbose_name': '院校logo'},
        ),
        migrations.AlterModelOptions(
            name='schoolinfo',
            options={'managed': True, 'verbose_name': '院校详情'},
        ),
        migrations.AlterModelOptions(
            name='schoolscore',
            options={'managed': True, 'verbose_name': '院校各科分数'},
        ),
        migrations.AlterModelOptions(
            name='sylbuild',
            options={'managed': True, 'verbose_name': '双一流建设'},
        ),
    ]