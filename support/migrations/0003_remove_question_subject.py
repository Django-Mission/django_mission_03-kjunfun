# Generated by Django 4.0.4 on 2022-04-17 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_rename_comment_faq'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='subject',
        ),
    ]
