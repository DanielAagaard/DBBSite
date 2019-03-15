# Generated by Django 2.1.7 on 2019-03-14 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='site',
            name='text',
        ),
        migrations.AddField(
            model_name='site',
            name='Rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='Title',
            field=models.CharField(default='Title', max_length=40, null='False', verbose_name='Movie title'),
            preserve_default='False',
        ),
        migrations.AddField(
            model_name='site',
            name='Year',
            field=models.CharField(max_length=4, null=True, verbose_name='Year'),
        ),
    ]