# Generated by Django 4.1.7 on 2023-05-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_collection', '0005_alter_booktitle_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktitle',
            name='cover',
            field=models.ImageField(default='images/placeholder_cover.png', null=True, upload_to='images/'),
        ),
    ]
