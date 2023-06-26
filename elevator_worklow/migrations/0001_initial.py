# Generated by Django 4.2.2 on 2023-06-26 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('elevator_name', models.CharField(max_length=100)),
                ('is_operational', models.BooleanField(default=True, help_text='Indicate whether the elevator is operational')),
                ('is_available', models.BooleanField(default=True, help_text='Indicate whether the elevator is available for use')),
                ('current_floor', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('UP', 'UP'), ('DOWN', 'DOWN'), ('STOPPED', 'STOPPED')], default='UP', help_text='Storing the current direction status', max_length=100)),
                ('door_status', models.CharField(choices=[('OPEN', 'OPEN'), ('CLOSE', 'CLOSE'), ('PARTIAL_OPEN', 'PARTIAL_OPEN')], default='OPEN', help_text='Storing the current door status', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElevatorSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total_elevators', models.PositiveIntegerField(default=0)),
                ('maintenance_mode', models.BooleanField(default=False, help_text='Indicate whether the elevator is maintaince mode or not')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('floor_number', models.IntegerField(unique=True)),
                ('elevator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='elevator', to='elevator_worklow.elevator')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('request_time', models.DateTimeField(auto_now_add=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('elevator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elevator_request', to='elevator_worklow.elevator')),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='floor_request', to='elevator_worklow.floor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='elevator',
            name='elevator_system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elevator_factory', to='elevator_worklow.elevatorsystem'),
        ),
    ]