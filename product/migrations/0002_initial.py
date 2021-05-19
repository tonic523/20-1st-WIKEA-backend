# Generated by Django 3.2.2 on 2021-05-19 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='comment',
            field=models.ManyToManyField(related_name='product', through='product.Comment', to='user.User'),
        ),
        migrations.AddField(
            model_name='product',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.series'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.subcategory'),
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='product.product'),
        ),
        migrations.AddField(
            model_name='description',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='description', to='product.product'),
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.product'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
