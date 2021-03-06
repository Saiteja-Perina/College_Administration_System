# Generated by Django 3.2 on 2021-05-14 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internals',
            fields=[
                ('internal_id', models.AutoField(primary_key=True, serialize=False)),
                ('sem', models.IntegerField()),
                ('sub_tot_marks', models.IntegerField(default=25)),
                ('sub_secured', models.IntegerField(default=0)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.department')),
                ('stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student')),
                ('sub_br_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subject')),
            ],
            options={
                'db_table': 'Internals',
                'unique_together': {('stud_id', 'sub_br_id')},
            },
        ),
    ]
