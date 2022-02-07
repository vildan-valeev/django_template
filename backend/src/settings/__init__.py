from split_settings.tools import include, optional

include(
    "base.py",
    "database.py",
    optional("local_settings.py"),
)
