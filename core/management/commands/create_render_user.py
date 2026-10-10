
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create the initial Render user securely"

    def handle(self, *args, **options):
        username = os.environ.get("RENDER_ADMIN_USERNAME")
        password = os.environ.get("RENDER_ADMIN_PASSWORD")

        if not username or not password:
            raise CommandError(
                "Set RENDER_ADMIN_USERNAME and "
                "RENDER_ADMIN_PASSWORD environment variables."
            )

        User = get_user_model()

        if User.objects.filter(username=username).exists():
            self.stdout.write("User already exists; no changes made.")
            return

        User.objects.create_superuser(
            username=username,
            email="",
            password=password,
        )

        self.stdout.write(
            self.style.SUCCESS("Render admin user created.")
        )
