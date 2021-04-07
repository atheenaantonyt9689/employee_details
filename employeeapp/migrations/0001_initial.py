# Generated by Django 3.1.5 on 2021-04-07 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('designation', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=10)),
            ],
        ),
    ]
