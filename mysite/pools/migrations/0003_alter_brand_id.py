# Generated by Django 4.2.1 on 2023-06-08 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0002_brand_alter_feedback_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
