# Generated by Django 4.0.4 on 2022-05-18 09:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MegazineCategories',
            fields=[
                ('CategoryID', models.IntegerField(primary_key=True, serialize=False)),
                ('CategoryName', models.CharField(max_length=255)),
                ('CategoryDiscription', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='MegazineDetails',
            fields=[
                ('MegazineID', models.IntegerField(primary_key=True, serialize=False)),
                ('MegazineCover', models.ImageField(upload_to='MegazineCover')),
                ('MegazineName', models.CharField(max_length=255)),
                ('MegazineDiscription', models.CharField(max_length=500)),
                ('RentPrice', models.IntegerField()),
                ('BuyPrice', models.IntegerField()),
                ('IssueDate', models.DateField()),
                ('Rating', models.IntegerField()),
                ('CategoryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.megazinecategories')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('fullname', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(max_length=10, unique=True)),
                ('tc', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
