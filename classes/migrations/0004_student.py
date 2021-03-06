# Generated by Django 3.1.1 on 2020-09-08 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_classroom_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=120)),
                ('exam_grade', models.DecimalField(decimal_places=3, max_digits=10)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.classroom')),
            ],
        ),
    ]
