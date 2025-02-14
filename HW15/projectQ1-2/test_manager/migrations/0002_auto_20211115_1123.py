# Generated by Django 3.2.9 on 2021-11-15 11:23

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('test_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
            ],
            managers=[
                ('people', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
