# Generated by Django 5.2 on 2025-05-13 04:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_project_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessingOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('algorithm', models.CharField(max_length=100)),
                ('parameters', models.JSONField(default=dict)),
                ('success', models.BooleanField(default=True)),
                ('error_message', models.TextField(blank=True, null=True)),
                ('execution_time_ms', models.IntegerField(default=0)),
                ('project_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operations', to='api.projectimage')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
