# Generated by Django 4.0.3 on 2022-03-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language_alter_author_options_alter_book_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(blank=True, help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)", max_length=200, null=True),
        ),
    ]
