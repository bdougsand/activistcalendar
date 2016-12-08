![ActivistCalendar Logo](https://raw.githubusercontent.com/ActCal/activistcalendar/master/ActivistCalendar.org%2C%20orange.jpg)
# activistcalendar.org [![Stories in Ready](https://badge.waffle.io/ActCal/activistcalendar.svg?label=ready&title=Ready)](http://waffle.io/ActCal/activistcalendar)

This repo is where activistcalendar.org is developed and deployed from!

## Overview
The mission of Activist Calendar is to strengthen Boston-based networks of organizers, artivists, hacktivists and engaged community members with tools and programming that support collaborations and community resource-building. We do this through our online calendar, social media (Facebook and Twitter) and in-person events (in development).

Activist Calendar will be an online calendar tool for activists to share their work and events around Boston. This searchable and sortable calendar will allow organizers to learn about each other and their work as a way to enable communication and collaboration. Community members can use the calendar to learn about groups, events and ways to engage.

While our web app is under development, we're actively sharing events out from our Facebook page. Follow us there to get info on upcoming activist events around Boston: https://www.facebook.com/activistcalendar

## Get involved!
If you're interested in finding out more about this project and how to get involved, email Loreto Paz Ansaldo (lpansaldo |at| gmail |.| com) and Lyre Calliope (lyre.calliope |at| gmail |.| com) and we'll help you get started!

### ActCal Community Members
* Write 'issues' for feature requests and bug reports: https://github.com/ActCal/activistcalendar/issues
* Check out and contribute to open issues: https://github.com/ActCal/activistcalendar/issues/new
* Send general feedback on the overall project to info@activistcalendar.org

### Software Developers

ActCal is currently being written in Python+Django with a PostgreSQL database.

Here’s how to set up a dev environment:
* Install git - https://git-scm.com/downloads
* Install PostgreSQL - version does not matter (9.3.2 preferred): https://www.postgresql.org/download/
* Install Python 2.7
* Install pip - https://pip.pypa.io/en/stable/installing/
* Install virtualenv: [http://docs.python-guide.org/en/latest/dev/virtualenvs/](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
* Initialize a virtual environment as per above
* (Next steps are within the virtual environment)
* Install: pip install psycopg2
* Install: pip install django==1.6.2
* Install: pip install django-uuidfield
* Clone the repo: [git@github.com](mailto:git@github.com):ActCal/activistcalendar.git
* Change directory: cd activistcalendar/activist
* Execute: python manage.py syncdb
* Execute: python manage.py runserver
* Server will live at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  - get that on your browser.

Once you’re set up, you’re ready to start working on issues! Check out the ‘ready’ column in our github integrated kanban board: [![Stories in Ready](https://badge.waffle.io/ActCal/activistcalendar.svg?label=ready&title=Ready)](http://waffle.io/ActCal/activistcalendar)


## Tutorials

Test-driven development is our jam. If you’re not familiar with this approach to writing software, check out these resources.
* Article: ‘Why We Use Test-Driven Development (TDD)’: https://quickleft.com/blog/use-test-driven-development-tdd/
* The literal book on ‘Test-Driven development with Python’: http://chimera.labs.oreilly.com/books/1234000000754/pt01.html

If you’re new to Python and Django
* Django Girls Tutorial [https://tutorial.djangogirls.org/en/](https://tutorial.djangogirls.org/en/)
* ‘Python for Ruby programmers’[ https://www.youtube.com/watch?v=maSlTKMzR3Q](https://www.youtube.com/watch?v=maSlTKMzR3Q)
* Moving to Pythong from other Languages
* [https://wiki.python.org/moin/MovingToPythonFromOtherLanguages](https://wiki.python.org/moin/MovingToPythonFromOtherLanguages)
* ‘Learn python in 10 minutes’ may be a useful quick reference: [https://www.stavros.io/tutorials/python/](https://www.stavros.io/tutorials/python/)
* Django tutorial: [https://docs.djangoproject.com/en/1.10/intro/](https://docs.djangoproject.com/en/1.10/intro/)

SQL and Object Relational Mapping (ORM)
* Django Girls - Django ORM and QuerySets https://tutorial.djangogirls.org/en/django_orm/
* What is an ORM: [http://hibernate.org/orm/what-is-an-orm/](http://hibernate.org/orm/what-is-an-orm/)
* PostgresSQL: [https://www.postgresql.org/docs/8.0/static/tutorial.html](https://www.postgresql.org/docs/8.0/static/tutorial.html)
* SQL in general: [http://www.tutorialspoint.com/sql/](http://www.tutorialspoint.com/sql/)
* Relational algebra: [https://www.tutorialspoint.com/dbms/relational_algebra.htm](https://www.tutorialspoint.com/dbms/relational_algebra.htm)

And if you’re new to web programming, the Mozilla Developer Network has some great tutorials:
* HTML: [https://developer.mozilla.org/en-US/docs/Learn/HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML)
* CSS: [https://developer.mozilla.org/en-US/docs/Web/CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* Javascript: [https://developer.mozilla.org/en-US/docs/Web/JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
