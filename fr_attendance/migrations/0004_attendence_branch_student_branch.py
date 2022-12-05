# Generated by Django 4.1.3 on 2022-12-05 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fr_attendance", "0003_rename_branch_attendence_courses_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="attendence",
            name="branch",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="student",
            name="branch",
            field=models.CharField(
                choices=[("CIS", "CIS"), ("EEC", "EEC")], max_length=100, null=True
            ),
        ),
    ]
