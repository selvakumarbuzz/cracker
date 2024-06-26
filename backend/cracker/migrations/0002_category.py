# Generated by Django 4.0.8 on 2024-04-07 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
                ('template', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cracker.template')),
            ],
        ),
    ]
