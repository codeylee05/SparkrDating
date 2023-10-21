# Generated by Django 4.2.4 on 2023-10-21 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparkrapp', '0003_profile_user_bio_profile_user_sexuality'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_profile_image',
            field=models.ImageField(default='media/defaults/def_prof_image.def_prof_image.jpg', upload_to='uploads/profile_images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_sexuality',
            field=models.CharField(choices=[('GAY', 'Gay'), ('HET', 'Heterosexual'), ('LES', 'Lesbian'), ('BIS', 'Bisexual'), ('PAN', 'Pansexual'), ('ASE', 'Asexual'), ('DEM', 'Demisexual'), ('QUE', 'Queer'), ('QUS', 'Questioning'), ('NON', 'Prefer Not To say')], default='NON', max_length=3),
        ),
    ]