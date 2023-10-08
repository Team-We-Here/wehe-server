# Generated by Django 4.2 on 2023-09-13 04:30

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userimage",
            name="image",
            field=models.ImageField(
                blank=True,
                default="profile_images/basic/profile_image3.webp",
                upload_to=user.models.UserImage.user_image_path,
                verbose_name="profile image",
            ),
        ),
    ]