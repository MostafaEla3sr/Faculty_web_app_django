# Generated by Django 4.1.1 on 2022-09-20 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_alter_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(default='photos/22/09/20/img2.jpg', upload_to='photos/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='teachingassistant',
            name='image',
            field=models.ImageField(default='photos/22/09/20/img2.jpg', upload_to='photos/%y/%m/%d'),
        ),
    ]
