# Generated by Django 4.0.8 on 2024-04-07 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cracker', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, default=99.99, max_digits=15)),
                ('availability', models.BooleanField(default=True)),
                ('is_offer', models.BooleanField(default=True)),
                ('image', models.ImageField(max_length=255, null=True, upload_to='product/%Y/%m/')),
                ('category', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cracker.category')),
                ('template', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cracker.template')),
            ],
        ),
    ]
