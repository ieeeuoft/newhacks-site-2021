# Generated by Django 3.2.5 on 2021-08-18 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0007_application_rsvp"),
    ]

    operations = [
        migrations.RemoveField(model_name="application", name="address_line_1",),
        migrations.RemoveField(model_name="application", name="address_line_2",),
        migrations.RemoveField(model_name="application", name="city",),
        migrations.RemoveField(model_name="application", name="postal_code",),
        migrations.RemoveField(model_name="application", name="q1",),
        migrations.RemoveField(model_name="application", name="q2",),
        migrations.RemoveField(model_name="application", name="q3",),
        migrations.RemoveField(model_name="application", name="state",),
        migrations.AddField(
            model_name="application",
            name="email_agree",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="I authorize MLH to send me pre- and post-event informational emails, which contain free credit and opportunities from their partners.",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="how_many_hackathons",
            field=models.TextField(
                choices=[
                    (None, ""),
                    ("1", "1"),
                    ("2", "2"),
                    ("3", "3"),
                    ("4", "4"),
                    ("5 or more", "5 or more"),
                ],
                default=0,
                help_text="How many hackathons have you been to?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="logistics_agree",
            field=models.BooleanField(
                default=False,
                help_text='I authorize you to share my application/registration information with Major League Hackingfor event administration, ranking, and MLH administration in-line with the <a href="https://mlh.io/privacy">MLH Privacy Policy</a>. I further agree to the terms of both the <a href="https://github.com/MLH/mlh-policies/tree/master/prize-terms-and-conditions">MLH Contest Terms and Conditions</a> and the <a href="https://mlh.io/privacy">MLH Privacy Policy.</a>',
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="referral_source",
            field=models.TextField(
                default="",
                help_text="How did you hear about NewHacks?",
                max_length=1000,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="tshirt_size",
            field=models.CharField(
                choices=[(None, ""), ("S", "S"), ("M", "M"), ("L", "L"), ("XL", "XL")],
                default="S",
                max_length=50,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="what_hackathon_experience",
            field=models.CharField(
                default="",
                help_text="If you???ve been to a hackathon, briefly tell us your experience. If not, describe what you expect to see and experience.",
                max_length=1000,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="what_technical_experience",
            field=models.TextField(
                default="",
                help_text="What is your technical experience with software and hardware? (1000 char max)",
                max_length=1000,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="why_participate",
            field=models.TextField(
                default="",
                help_text="Why do you want to participate in NewHacks? (1000 char max)",
                max_length=1000,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="application",
            name="conduct_agree",
            field=models.BooleanField(
                help_text='I have read and agree to the <a href="https://static.mlh.io/docs/mlh-code-of-conduct.pdf">MLH code of conduct</a>.'
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="data_agree",
            field=models.BooleanField(
                blank=True,
                help_text="I consent to IEEE UofT sharing my resume with event sponsors.",
            ),
        ),
    ]
