# Generated by Django 4.0.2 on 2022-07-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_credit_grndtot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='taxamnt',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
