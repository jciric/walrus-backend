# Generated by Django 2.2.2 on 2019-06-28 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0006_auto_20190628_0743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Music', 'music'), ('Painting&Drawing', 'painting&drawing'), ('Photography', 'photography')], default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_created', models.DateField(auto_now=True)),
                ('owner', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='users.users')),
                ('tag', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]