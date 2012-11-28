from fabric.api import *
from conf import hosts as hosts_conf
from fabfile import ycsb

@roles('server')
def df():
    """Shows the free disk space on servers"""
    run('df -h')

@hosts(hosts_conf.env.roledefs['server'][0])
def db_status(db):
    """Shows the status of the DB"""
    database = ycsb._getdb(db)
    with settings(hide('stdout'), hosts=database['status']['hosts']):
        print run(database['status']['command'])
