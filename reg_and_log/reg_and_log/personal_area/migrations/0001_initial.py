# Generated by Django 4.2.1 on 2023-05-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
