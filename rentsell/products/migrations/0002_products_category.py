# Generated by Django 5.0.6 on 2024-06-17 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
