# Generated by Django 4.0.3 on 2022-04-30 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0012_remove_faq_answer_remove_faq_question_faq_subject_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('general', '일반'), ('account', '계정'), ('etc', '기타')], max_length=8, null=True, verbose_name='카테고리')),
                ('subject', models.CharField(default='', max_length=200, null=True, verbose_name='제목')),
                ('useremail', models.EmailField(max_length=128, verbose_name='사용자이메일')),
                ('phone_number', models.CharField(max_length=12)),
                ('content', models.TextField(verbose_name='내용')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='작성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='최종수정일')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.faq')),
            ],
        ),
    ]
