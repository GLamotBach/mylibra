# Generated by Django 4.1.7 on 2023-06-18 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public_profile', '0005_alter_userspublicprofile_image'),
        ('friend_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendinvite',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='public_profile.userspublicprofile'),
        ),
        migrations.AlterField(
            model_name='friendinvite',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='public_profile.userspublicprofile'),
        ),
    ]
