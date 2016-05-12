from charms.reactive import when, set_state
from charmhelpers.core.hookenv import status_set
from subprocess import check_call


def sh(command):
    check_call(command, shell=True)


@when('apache.available')
def start_wiki():
    sh("chmod -R a+w /var/www/mywiki/conf")
    sh("chmod -R a+w /var/www/mywiki/data")
    set_state('apache.start')
    status_set('active', 'Ready')
