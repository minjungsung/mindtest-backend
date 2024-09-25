#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from django.core.management.commands.runserver import Command as runserver


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sitebase.settings")
    ...

if __name__ == "__main__":
    main()
