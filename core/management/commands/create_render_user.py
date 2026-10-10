

import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create or update the initial Render admin user"

    def handle(self, *args, **options):
        username = os.environ.get("RENDER_ADMIN_USERNAME")
        password = os.environ.get("RENDER_ADMIN_PASSWORD")

        if not username or not password:
            raise CommandError(
                "Set RENDER_ADMIN_USERNAME and "
                "RENDER_ADMIN_PASSWORD environment variables."
            )

        User = get_user_model()
        user, created = User.objects.get_or_create(
            username=username,
            defaults={"email": ""},
        )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"Render admin user {'created' if created else 'updated'}."
            )
        )

