# Generated by Django 3.1.7 on 2021-03-28 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
