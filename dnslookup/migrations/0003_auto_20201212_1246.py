# Generated by Django 3.1.3 on 2020-12-12 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnslookup', '0002_searcheddomains'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='Descriptions',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='country',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='email',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='instagram',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='options',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='phone',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='twitter',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
