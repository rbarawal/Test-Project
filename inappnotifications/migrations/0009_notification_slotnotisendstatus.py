# Generated by Django 3.2.4 on 2023-09-02 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inappnotifications', '0008_emailtemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='slotnotisendstatus',
            field=models.BooleanField(default=False),
        ),
    ]