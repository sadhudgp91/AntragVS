# Generated by Django 2.2.3 on 2019-07-17 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='grunddaten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sapkonto', models.TextField()),
                ('vorname', models.TextField()),
                ('idj', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='sapname',
            field=models.TextField(),
        ),
    ]
