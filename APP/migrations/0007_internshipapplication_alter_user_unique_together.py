# Generated by Django 5.0.6 on 2024-06-09 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0006_alter_user_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternshipApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('domain', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('resume', models.FileField(upload_to='resumes/')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set(),
        ),
    ]