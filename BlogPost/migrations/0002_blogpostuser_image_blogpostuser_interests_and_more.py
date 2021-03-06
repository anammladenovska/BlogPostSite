# Generated by Django 4.0.4 on 2022-06-02 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpostuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
        migrations.AddField(
            model_name='blogpostuser',
            name='interests',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='blogpostuser',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='blogpostuser',
            name='profession',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='blogpostuser',
            name='skills',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='blogpostuser',
            name='surname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
