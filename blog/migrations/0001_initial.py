# Generated by Django 4.2.6 on 2023-10-21 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='заголовок')),
                ('slug', models.CharField(blank=True, max_length=200, null=True, verbose_name='slug')),
                ('content', models.TextField(verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='articles/', verbose_name='превью')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='признак публикации')),
                ('views_count', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]
