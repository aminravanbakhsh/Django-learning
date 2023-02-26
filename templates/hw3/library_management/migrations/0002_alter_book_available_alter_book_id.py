# Generated by Django 4.1.5 on 2023-02-26 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='available',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]