# Generated by Django 3.0.4 on 2020-03-12 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scouter_id', models.PositiveSmallIntegerField()),
                ('match_number', models.PositiveSmallIntegerField()),
                ('team_number', models.PositiveSmallIntegerField()),
                ('total_balls_preloaded', models.PositiveSmallIntegerField()),
                ('crossed_initiation_line', models.BooleanField()),
                ('total_bottom_auto_scored', models.PositiveSmallIntegerField()),
                ('total_outer_auto_scored', models.PositiveSmallIntegerField()),
                ('total_inner_auto_scored', models.PositiveSmallIntegerField()),
                ('total_bottom_teleop_scored', models.PositiveSmallIntegerField()),
                ('total_outer_teleop_scored', models.PositiveSmallIntegerField()),
                ('total_inner_teleop_scored', models.PositiveSmallIntegerField()),
                ('shoots_close', models.BooleanField()),
                ('shoots_mid', models.BooleanField()),
                ('shoots_trench', models.BooleanField()),
                ('total_rotation_tries', models.PositiveSmallIntegerField()),
                ('rotation_succeeded', models.BooleanField()),
                ('total_position_tries', models.PositiveSmallIntegerField()),
                ('position_succeeded', models.BooleanField()),
                ('climb_height', models.PositiveSmallIntegerField(choices=[(0, 'None'), (1, 'Low'), (2, 'Middle'), (3, 'High')])),
                ('climb_position', models.CharField(choices=[('N', 'None'), ('C', 'Center'), ('S', 'Side')], max_length=1)),
                ('parked', models.BooleanField()),
                ('fell_down', models.BooleanField()),
                ('buddy_climb', models.PositiveSmallIntegerField(choices=[(0, 'None'), (2, 'Successfully Lifted 2 Others'), (1, 'Successfully Lifted 1 Other'), (-1, 'Got Lifted Successfully')])),
                ('adjusts_position_on_bar', models.BooleanField()),
                ('defense_played', models.PositiveSmallIntegerField(choices=[(0, 'No defense'), (1, 'Poor defense'), (2, 'Moderate defense'), (3, 'Good defense')])),
                ('defense_handling', models.PositiveSmallIntegerField(choices=[(0, 'Not defended against'), (1, 'Handled defense poorly'), (2, 'Handled defense moderately'), (3, 'Handled defense well')])),
                ('has_technical_issues', models.BooleanField()),
                ('comments', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scouter_id', models.PositiveSmallIntegerField()),
                ('team_number', models.PositiveSmallIntegerField()),
                ('drive_train', models.CharField(choices=[('S', 'Swerve'), ('W', 'West Coast Drive'), ('M', 'Mecanum'), ('H', 'H-Drive'), ('OD', 'Omni Drive'), ('O', 'Other')], max_length=2)),
                ('outtake_bottom', models.BooleanField()),
                ('outtake_outer', models.BooleanField()),
                ('outtake_inner', models.BooleanField()),
                ('ground_intake', models.BooleanField()),
                ('port_intake', models.BooleanField()),
                ('robot_intake', models.BooleanField()),
                ('climb_level', models.PositiveSmallIntegerField(choices=[(1, 'Low Climb'), (2, 'Middle Climb'), (3, 'High Climb')])),
                ('buddy_climb', models.PositiveSmallIntegerField(choices=[(0, 'None'), (1, 'Carry 1 Other'), (2, 'Carry 2 Others')])),
            ],
        ),
    ]
