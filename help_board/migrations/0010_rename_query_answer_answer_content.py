# Generated by Django 4.2.9 on 2024-02-14 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('help_board', '0009_alter_answer_options_remove_query_excerpt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='query_answer',
            new_name='content',
        ),
    ]
