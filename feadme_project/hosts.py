from django_hosts import patterns, host

host_patterns = patterns('feadme_project',
    host(r'api', 'urls', name='api'),
    host(r'beta', 'urls', name='www'),
)
