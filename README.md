# Test a wagtail struct block default with an image block 

How to test
1. `uv sync`
2. `uv run python manage.py makemigrations --check --noinput` --> should not raise an exception, even without image defined
3. `uv run python.manage.py migrate`
4. `uv run python manage.py createsuperuser`
5. `uv run python manage.py runserver`
6. Go create an image in wagtail admin
7. Add an item in homepage streamfield

The image block should be pre-populated
