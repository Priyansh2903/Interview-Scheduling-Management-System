# Generated by Django 4.2.5 on 2023-09-18 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("candidates", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="InterviewSchedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("interview_date", models.DateField()),
                ("mode", models.CharField(max_length=20)),
                ("venue", models.TextField(blank=True, null=True)),
                (
                    "candidate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="candidates.candidate",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InterviewObservation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("interview_marks", models.IntegerField()),
                ("notice_period", models.IntegerField()),
                (
                    "interview",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="interviews.interviewschedule",
                    ),
                ),
            ],
        ),
    ]
