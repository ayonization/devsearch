# Generated by Django 4.1.3 on 2022-11-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_tag_project_vote_ratio_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
