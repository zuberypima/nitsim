# Generated by Django 4.2.1 on 2023-05-27 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regitraer', '0002_regnumber_alter_student_registrtionno'),
        ('teacher', '0004_remove_caresult_id_alter_caresult_registrationno'),
    ]

    operations = [
        migrations.AddField(
            model_name='caresult',
            name='id',
            field=models.UUIDField(default=2752023, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='caresult',
            name='registrationNo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='regitraer.regnumber'),
        ),
    ]
