# Generated by Django 3.0.5 on 2020-04-29 04:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('kakao_id', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='UserID')),
                ('email', models.EmailField(max_length=254, null=True, unique=True, verbose_name='이메일')),
                ('nickname', models.CharField(max_length=20, unique=True, verbose_name='닉네임')),
                ('item', models.CharField(max_length=50, null=True, verbose_name='유저 물건')),
                ('price', models.IntegerField(null=True, verbose_name='물건가격')),
                ('monthly_cost', models.IntegerField(null=True, verbose_name='한달 식비')),
                ('profile_image', models.CharField(max_length=255, null=True, verbose_name='프로필사진')),
                ('item_image', models.CharField(max_length=255, null=True, verbose_name='물건 사진')),
                ('ages', models.IntegerField(null=True, verbose_name='나이')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(auto_now_add=True, null=True)),
                ('user_breakfast', models.IntegerField(blank=True, default=0, null=True)),
                ('user_lunch', models.IntegerField(blank=True, default=0, null=True)),
                ('user_dinner', models.IntegerField(blank=True, default=0, null=True)),
                ('total_paid', models.IntegerField(blank=True, null=True)),
                ('today_saving', models.IntegerField(blank=True, null=True)),
                ('kakao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
