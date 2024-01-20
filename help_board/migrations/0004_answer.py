# Generated by Django 4.2.9 on 2024-01-20 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('help_board', '0003_query_updated_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_answer', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answered_by', to=settings.AUTH_USER_MODEL)),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='query_asked', to='help_board.query')),
            ],
        ),
    ]
