# Generated by Django 5.0.4 on 2024-04-30 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_citizenchip_no_confirmationpersondetail_citizenship_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
