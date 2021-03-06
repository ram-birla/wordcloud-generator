# Generated by Django 2.2.3 on 2020-05-18 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Simple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.FileField(upload_to='cloud/stext/')),
                ('cloud', models.ImageField(blank=True, default='', null=True, upload_to='cloud/result/')),
            ],
        ),
        migrations.AddField(
            model_name='wrdcloud',
            name='cloud',
            field=models.ImageField(blank=True, default='', null=True, upload_to='cloud/result/'),
        ),
    ]
