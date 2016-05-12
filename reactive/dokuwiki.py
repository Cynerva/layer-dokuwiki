from charms.reactive import when, set_state
from charmhelpers.core.hookenv import status_set
from subprocess import check_call


def sh(command):
    check_call(command.split())


@when('apache.available')
def start_wiki():
    sh("chown -R www-data:www-data /var/www/mywiki")
    set_state('apache.start')
    status_set('active', 'Ready')
