# Generated by Django 3.1.1 on 2020-09-11 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paging', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('id',)},
        ),
    ]
