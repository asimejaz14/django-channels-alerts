# Generated by Django 5.0.3 on 2024-03-20 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banklogs',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='banklogsutc',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]