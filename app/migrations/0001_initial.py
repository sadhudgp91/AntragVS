# Generated by Django 2.2.3 on 2019-07-03 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sapname', models.TextField(max_length=300, unique=True)),
                ('vorname', models.TextField()),
            ],
        ),
    ]
