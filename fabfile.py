import os
import sys
from fabric.api import *
from fabric.context_managers import env

try:
    os.environ['ANSIBLE_HOST']
    os.environ['ANSIBLE_REMOTE_USER']
    os.environ['ANSIBLE_REMOTE_USER_PASS']
except KeyError:
    print "Please set the environment variables ANSIBLE_HOST, ANSIBLE_REMOTE_USER"
    sys.exit(1)

# Remote host
env.hosts = [os.environ['ANSIBLE_HOST']]
# Remote user
env.user = os.environ['ANSIBLE_REMOTE_USER']
# User password
env.password = os.environ['ANSIBLE_REMOTE_USER_PASS']
# Ssh keys directory on local and remote hosts
env.ssh_key_dir = '~/.ssh'

env.new_user = 'ansible'
env.new_user_grp = 'ansiblegr'


def bootstrap():
    env.ssh_key_filepath = os.path.join(env.ssh_key_dir, env.host_string + "_ssh_key")
    local('ssh-keygen -t rsa -b 2048 -f {}'.format(env.ssh_key_filepath))
    upload_keys(env.user)
    # _create_privileged_group()
    # _create_privileged_user()
    run('service ssh reload')


def _create_privileged_group():
    run('/usr/sbin/groupadd ' + env.new_user_grp)
    run('mv /etc/sudoers /etc/sudoers-backup')
    run('(cat /etc/sudoers-backup ; echo "%' + env.new_user_grp \
        + ' ALL=(ALL) ALL") > /etc/sudoers')
    run('chmod 440 /etc/sudoers')


def _create_privileged_user():
    run('/usr/sbin/useradd -c "%s" -m -g %s %s' % \
        (env.new_user_full_name, env.new_user_grp, env.new_user))
    run('/usr/bin/passwd %s' % env.new_user)
    run('/usr/sbin/usermod -a -G ' + env.new_user_grp + ' ' + \
        env.new_user)
    run('mkdir /home/%s/.ssh' % env.new_user)
    run('chown -R %s /home/%s/.ssh' % (env.new_user,
                                       env.new_user))
    run('chgrp -R %s /home/%s/.ssh' % (env.new_user_grp,
                                       env.new_user))


def upload_keys(username):
    scp_command = "scp {} {}@{}:~/.ssh/".format(
        env.ssh_key_filepath + ".pub",
        username,
        env.host_string
    )
    ssh_copy_id_command = "ssh-copy-id -i {} {}@{}".format(
        env.ssh_key_filepath + ".pub",
        username,
        env.host_string
    )
    local(scp_command)
    local(ssh_copy_id_command)
