# Generated by Django 4.1 on 2022-09-06 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.TextField(blank=True, null=True),
        ),
    ]
