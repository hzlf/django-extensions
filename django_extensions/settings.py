import os

from django.conf import settings

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
REPLACEMENTS = {
}
add_replacements = getattr(settings, 'EXTENSIONS_REPLACEMENTS', {})
REPLACEMENTS.update(add_replacements)
MAX_UNIQUE_QUERY_ATTEMPTS = getattr(settings, 'AUTO_SLUG_FIELD_MAX_UNIQUE_QUERY_ATTEMPTS', 100)
