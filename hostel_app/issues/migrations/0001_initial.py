# Generated by Django 4.1.1 on 2022-09-16 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_data',
            fields=[
                ('Name', models.CharField(default='xyz', max_length=50)),
                ('mobile', models.CharField(max_length=15)),
                ('regno', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('roomno', models.CharField(max_length=3)),
                ('floorno', models.CharField(max_length=3)),
                ('block', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name': 'student_data',
            },
        ),
        migrations.CreateModel(
            name='all_issues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=2000)),
                ('upvote', models.CharField(default='1', max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('regno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issues.student_data')),
            ],
        ),
    ]
