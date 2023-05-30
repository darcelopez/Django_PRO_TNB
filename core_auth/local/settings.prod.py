DEBUG = False
SECRET_KEY = 'django-insecure-a%v3^ql(=z+w81!r%4pug7+qtch-og+4g@vg+#!t+x#2kxv&f^'

LOGGING['formatters']['colored'] = {  # type: ignore
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
}
LOGGING['loggers']['core']['level'] = 'DEBUG'  # type: ignore
LOGGING['handlers']['console']['level'] = 'DEBUG'  # type: ignore
LOGGING['handlers']['console']['formatter'] = 'colored'  # type: ignore

print('Finish preparing settings. DEBUG FALSE')
