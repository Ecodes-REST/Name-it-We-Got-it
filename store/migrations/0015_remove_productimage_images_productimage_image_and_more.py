# Generated by Django 4.2.6 on 2023-10-27 11:42

from django.db import migrations, models
import django.db.models.deletion
import store.validators
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='images',
        ),
        migrations.AddField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default='playground/images.jpg', upload_to='store/images', validators=[store.validators.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.product'),
        ),
    ]
