## South

Mini-Howto:
* Data is already existing

    python manage.py migrate <app> 001 --fake
    python manage.py migrate

* Model was changed

    python manage.py schemamigration --auto <app>
    python manage.py migrate <app>

* Start with a new Site without any data (do not use migrations)

    python manage.py syncdb --all
