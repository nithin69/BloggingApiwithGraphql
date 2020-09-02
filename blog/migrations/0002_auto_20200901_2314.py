# Generated by Django 3.1.1 on 2020-09-01 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='commented_on',
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.comment'),
        ),
    ]