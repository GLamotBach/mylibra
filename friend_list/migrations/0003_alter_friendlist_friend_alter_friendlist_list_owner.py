# Generated by Django 4.1.7 on 2023-06-19 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public_profile', '0005_alter_userspublicprofile_image'),
        ('friend_list', '0002_alter_friendinvite_from_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendlist',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend', to='public_profile.userspublicprofile'),
        ),
        migrations.AlterField(
            model_name='friendlist',
            name='list_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_owner', to='public_profile.userspublicprofile'),
        ),
    ]
