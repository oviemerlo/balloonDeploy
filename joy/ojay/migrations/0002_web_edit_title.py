# Generated by Django 3.2.18 on 2023-04-20 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ojay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='web_edit',
            name='title',
            field=models.TextField(default='name of design'),
        ),
    ]