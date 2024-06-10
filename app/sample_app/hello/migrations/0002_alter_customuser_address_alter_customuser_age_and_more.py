# Generated by Django 4.2 on 2024-06-03 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hello", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="address",
            field=models.TextField(blank=True, null=True, verbose_name="住所"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="age",
            field=models.IntegerField(blank=True, null=True, verbose_name="年齢"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="birth_date",
            field=models.DateField(blank=True, null=True, verbose_name="生年月日"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="gender",
            field=models.CharField(default=2, max_length=1, verbose_name="性別"),
        ),
    ]
