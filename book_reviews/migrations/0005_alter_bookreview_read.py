# Generated by Django 4.1.7 on 2023-07-04 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_reviews', '0004_bookrating_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='read',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book_reviews.readbook'),
        ),
    ]
