# Generated by Django 3.0.8 on 2020-08-02 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
            ],
        ),
    ]
