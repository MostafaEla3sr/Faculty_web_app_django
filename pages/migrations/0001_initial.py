# Generated by Django 4.1.1 on 2022-09-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='user', max_length=50, verbose_name='Name')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('image', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('description', models.TextField()),
                ('specialization', models.CharField(choices=[('Student', 'Student'), ('Doctor', 'Doctor'), ('Teaching Assistant', 'Teaching Assistant'), ('Employee', 'Employee')], max_length=50, null=True)),
                ('birthDate', models.DateField(null=True)),
            ],
            options={
                'verbose_name': 'user',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('specialization', models.CharField(choices=[('CS', 'CS'), ('IS', 'IS'), ('IT', 'IT')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Subject Name')),
                ('hours', models.IntegerField(default=3, verbose_name='Subject hours')),
            ],
        ),
        migrations.CreateModel(
            name='TeachingAssistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('students', models.ManyToManyField(to='pages.profile')),
            ],
        ),
    ]