# Generated by Django 4.0.2 on 2022-07-23 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_salesrecpts_tax2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='grndtot',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
