# Generated by Django 4.2.1 on 2023-05-27 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regitraer', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='programName',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='regitraer.programreg'),
        ),
    ]