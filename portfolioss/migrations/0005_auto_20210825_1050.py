# Generated by Django 3.1.5 on 2021-08-25 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioss', '0004_auto_20210825_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suscriber',
            old_name='emails',
            new_name='email',
        ),
    ]
