# Generated by Django 4.2.7 on 2024-07-06 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dpr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datawithschool',
            name='data',
        ),
        migrations.DeleteModel(
            name='Data',
        ),
        migrations.DeleteModel(
            name='DataWithSchool',
        ),
    ]
