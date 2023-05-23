# Generated by Django 4.2.1 on 2023-05-23 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regitraer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalmarks', models.ImageField(blank=True, null=True, upload_to='')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regitraer.courseregitration')),
                ('examtype', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='regitraer.regnumber')),
                ('programname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regitraer.programreg')),
            ],
        ),
    ]