# Generated by Django 4.1.7 on 2023-06-09 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_imagerecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagerecord',
            name='caption',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagerecord',
            name='description',
            field=models.TextField(),
        ),
    ]