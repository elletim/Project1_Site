# Generated by Django 3.2.15 on 2022-10-02 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_url',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Url',
        ),
    ]