# Generated by Django 5.1.1 on 2024-09-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_id_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.TextField(max_length=1000)),
                ('emailid', models.CharField(max_length=1001)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        )
    ]
