from setuptools import setup


setup(
    name="Trackman",
    py_modules=["trackman"],
    description="Advanced track logging",
    license="AGPL3",
    author="Trackman authors",
    keywords="wuvt",
    url="https://github.com/wuvt/trackman",
    install_requires=[
        "celery",
        "click",
        "Flask",
        "Flask-Migrate",
        "flask-oidc",
        "Flask-RESTful",
        "Flask-SQLAlchemy",
        "Flask-WTF",
        "humanize",
        "Markdown",
        "musicbrainzngs",
        "netaddr",
        "passlib",
        "psycopg2",
        "pyasn1",
        "pyasn1-modules",
        "PyMySQL",
        "python-dateutil",
        "python-editor",
        "python-redis-lock",
        "pytz",
        "redis",
        "requests",
        "SQLAlchemy-Utils",
        "Unidecode",
    ],
    dependency_links=[
        "git+https://github.com/wuvt/python-musicbrainzngs#egg=musicbrainzngs",
    ],
)
