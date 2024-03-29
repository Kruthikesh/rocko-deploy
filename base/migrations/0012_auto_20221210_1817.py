# Generated by Django 3.2.9 on 2022-12-10 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_team_previousperformance'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=124, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='phoneNumber',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
