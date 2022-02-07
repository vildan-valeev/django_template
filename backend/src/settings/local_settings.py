from src.settings.base import BASE_DIR, env

print(env.str("SQL_DATABASE"), 'SQL_DATABASE!!!!!!!!!!!')
print(env.str("SQL_ENGINE"), 'SQL_DATABASE!!!!!!!!!!!')

DATABASES = {'default': {
    'ENGINE': env.str("SQL_ENGINE"),
    'NAME': BASE_DIR / env.str("SQL_DATABASE"),
}
}
