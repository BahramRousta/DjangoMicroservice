# Generated by Django 4.2 on 2023-04-17 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=500)),
                ('slug', models.SlugField(max_length=500, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('published', models.DateField()),
                ('category_id', models.IntegerField(null=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('new_publish', models.BooleanField(blank=True, default=False, null=True)),
                ('available', models.BooleanField(blank=True, default=True, null=True)),
                ('count_sold', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'ordering': ['-published'],
            },
        ),
    ]
