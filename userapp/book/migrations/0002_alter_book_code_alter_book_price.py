# Generated by Django 5.1.4 on 2025-01-17 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='code',
            field=models.IntegerField(help_text='코드는 숫자 4자리로 작성하세요', unique=True, verbose_name='도서코드'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(help_text='최소 1000 이상이어야 합니다.', verbose_name='도서가격'),
        ),
    ]
