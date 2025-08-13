from django.db import migrations
from django.contrib.auth.models import Group

def create_groups(apps, schema_editor):
    # Create the groups if they do not already exist
    Group.objects.get_or_create(name='admin')
    Group.objects.get_or_create(name='guest')
    Group.objects.get_or_create(name='creator')

class Migration(migrations.Migration):

    dependencies = [
        ('linkverse', '0001_initial'),  # Update with the latest migration file
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
