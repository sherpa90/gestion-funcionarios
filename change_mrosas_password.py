#!/usr/bin/env python3
"""Script to change password for mrosas user"""

import os
import django
from django.contrib.auth import get_user_model

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

User = get_user_model()

try:
    user = User.objects.get(email='mrosas@losalercespuertomontt.cl')
    new_password = 'Mrosas12345!'
    user.set_password(new_password)
    user.save()
    print("Password changed successfully for mrosas")
except User.DoesNotExist:
    print("User mrosas@losalercespuertomontt.cl not found")
except Exception as e:
    print(f"Error: {e}")
