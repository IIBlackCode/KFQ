# Generated by Django 3.2.4 on 2021-07-06 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
