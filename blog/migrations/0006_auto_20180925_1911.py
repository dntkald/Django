# Generated by Django 2.1.1 on 2018-09-25 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180916_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='author',
        ),
        migrations.DeleteModel(
            name='Diary',
        ),
    ]