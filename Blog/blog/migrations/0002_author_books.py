# Generated by Django 4.1 on 2022-09-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
