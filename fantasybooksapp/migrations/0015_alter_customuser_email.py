# Generated by Django 5.0.7 on 2024-08-04 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasybooksapp', '0014_remove_customuser_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=30, unique=True),
        ),
    ]
