import os
from fabric.api import *

env.guest_user = 'ubuntu'
env.hosts = '192.168.50.11'
env.ssh_key_dir = '~/.ssh'


def bootstrap():
    print env
    env.ssh_key_filepath = os.path.join(env.ssh_key_dir, env.host_string + "_key")
    local('ssh-keygen -t rsa -b 2048 -f {}'.format(env.ssh_key_filepath))
    local('cp {} {}/authorized_keys'.format(env.ssh_key_filepath + ".pub", env.ssh_key_dir))
    upload_keys(env.guest_user)
    run('service ssh reload')


def upload_keys(username):
    scp_command = "scp {} {}/authorized_keys {}@{}:~/.ssh".format(
        env.ssh_key_filepath + ".pub",
        env.ssh_key_dir,
        username,
        env.host_string
    )
    local(scp_command)
