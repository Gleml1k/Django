# Generated by Django 4.2.1 on 2023-05-20 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('text', models.TextField(max_length=1000)),
                ('author', models.CharField(max_length=40)),
                ('data', models.DateField()),
            ],
        ),
    ]
