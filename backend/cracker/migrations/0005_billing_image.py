# Generated by Django 4.0.8 on 2024-04-07 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cracker', '0004_billing'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='image',
            field=models.ImageField(max_length=255, null=True, upload_to='billing/%Y/%m/'),
        ),
    ]
