# Generated by Django 4.1.7 on 2023-07-04 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_reviews', '0003_bookrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookrating',
            name='read',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='book_reviews.readbook'),
            preserve_default=False,
        ),
    ]