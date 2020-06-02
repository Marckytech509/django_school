# Generated by Django 2.2.12 on 2020-05-29 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20200528_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ('classe_name',),
            },
        ),
        migrations.RemoveField(
            model_name='review',
            name='course',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user_name',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='overview',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='owner',
            new_name='prof',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='title',
            new_name='titre',
        ),
        migrations.RenameField(
            model_name='module',
            old_name='title',
            new_name='titre',
        ),
        migrations.RemoveField(
            model_name='course',
            name='image',
        ),
        migrations.RemoveField(
            model_name='course',
            name='subject',
        ),
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='courses_joined', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CourseImg',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.AddField(
            model_name='course',
            name='classe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='course.Classe'),
            preserve_default=False,
        ),
    ]