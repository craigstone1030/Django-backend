# Generated by Django 3.2.5 on 2021-08-19 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_alter_user_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='cga_user',
        ),
    ]