# Generated by Django 3.2.5 on 2021-07-31 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_auto_20210731_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='q4',
            field=models.TextField(help_text='What is your technical experience with software and hardware? (1000 char max)', max_length=1000),
        ),
    ]
