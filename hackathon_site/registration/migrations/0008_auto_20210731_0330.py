# Generated by Django 3.2.5 on 2021-07-31 07:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0007_application_rsvp"),
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="email_agree",
            field=models.BooleanField(
                default=True,
                help_text="I authorize MLH to send me pre- and post-event informational emails, which contain free credit and opportunities from their partners.",
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="logistics_agree",
            field=models.BooleanField(
                default=True,
                help_text='I authorize you to share my application/registration information with Major League Hackingfor event administration, ranking, and MLH administration in-line with the <a href="https://mlh.io/privacy">MLH Privacy Policy</a>. I further agree to the terms of both the <a href="https://github.com/MLH/mlh-policies/tree/master/prize-terms-and-conditions">MLH Contest Terms and Conditions</a> and the <a href="https://mlh.io/privacy">MLH Privacy Policy.</a>',
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="q4",
            field=models.TextField(
                default=django.utils.timezone.now,
                help_text="What is your technical experience with software and hardware? (1000 char max)",
                max_length=100,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="q5",
            field=models.TextField(
                default=django.utils.timezone.now,
                help_text="How did you hear about NewHacks?",
                max_length=1000,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="tshirt_size",
            field=models.CharField(
                choices=[
                    ("small", "S"),
                    ("medium", "M"),
                    ("large", "L"),
                    ("extra-large", "XL"),
                ],
                default=django.utils.timezone.now,
                max_length=50,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="application",
            name="conduct_agree",
            field=models.BooleanField(
                help_text='I have read and agree to the <a href="https://docs.google.com/document/d/1Uec_PDknY-9nSMc7QOqSTFb54I71uGX6oZaoTm1u8Q0/">MLH code of conduct</a>.'
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="data_agree",
            field=models.BooleanField(
                help_text="I consent to IEEE UofT sharing my resume with event sponsors."
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="q1",
            field=models.TextField(
                choices=[
                    ("one", "1"),
                    ("two", "2"),
                    ("three", "3"),
                    ("four", "4"),
                    ("five_more", "5 or more"),
                ],
                help_text="How many hackathons have you been to?",
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="q2",
            field=models.TextField(
                help_text="If you’ve been to a hackathon, briefly tell us your experience. If not, describe what you expect to see and experience. (1000 char max)",
                max_length=1000,
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="q3",
            field=models.TextField(
                help_text="Why do you want to participate in NewHacks? (1000 char max)",
                max_length=1000,
            ),
        ),
    ]
