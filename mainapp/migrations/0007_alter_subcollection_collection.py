# Generated by Django 4.0.4 on 2022-04-13 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_userchatid_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcollection',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.collection', verbose_name='Категория'),
        ),
    ]
