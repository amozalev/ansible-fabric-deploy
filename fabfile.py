import os
from fabric.api import *

env.guest_user = 'ubuntu'
env.hosts = '192.168.50.11'
env.ssh_key_dir = '~/.ssh'
env.password = 'ubuntu'
jenkins_output_folder = ''


def bootstrap():
    copy_jenkins_output_files()

    env.ssh_key_filepath = os.path.join(env.ssh_key_dir, env.host_string + "_key")
    local('ssh-keygen -t rsa -b 2048 -f {}'.format(env.ssh_key_filepath))
    upload_keys(env.guest_user)
    run('service ssh reload')


def copy_jenkins_output_files():
    local('cp {}application.properties ./roles/mobile_connector/files/'.format(jenkins_output_folder))
    local('cp {}mobile_connector-1.0-SNAPSHOT.jar ./roles/mobile_connector/files/'.format(jenkins_output_folder))


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
