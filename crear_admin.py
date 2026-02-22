#!/usr/bin/env python
"""
Script para crear un usuario administrador
Usage: python crear_admin.py
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from users.models import CustomUser

def crear_admin():
    email = 'mrosas@losalercespuertomontt.cl'
    run = '12345678-5'  # RUT de ejemplo - cámbialo si es necesario
    password = 'Sgpal2025!'  # Nueva contraseña
    
    try:
        # Verificar si el usuario ya existe
        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            user.is_superuser = True
            user.is_staff = True
            user.role = 'ADMIN'
            user.set_password(password)
            user.save()
            print(f"Usuario {email} actualizado a administrador.")
        else:
            user = CustomUser(
                email=email,
                run=run,
                first_name='Marcelo',
                last_name='Rosas',
                is_superuser=True,
                is_staff=True,
                role='ADMIN'
            )
            user.set_password(password)
            user.save()
            print(f"Usuario administrador creado: {email}")
            print(f"Contraseña: {password}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    crear_admin()
