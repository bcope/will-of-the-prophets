# Generated by Django 2.1.1 on 2018-09-26 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('will_of_the_prophets', '0003_s3direct'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialsquaretype',
            name='auto_move',
            field=models.IntegerField(default=0, help_text='Automatically move the runabout by this many places'),
        ),
    ]
