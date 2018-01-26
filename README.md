# ansible-java-deploy
Generates ssh keys for remote host and installs a set of packages (git, java, Russian locale, nano, postgresql, 
tomcat, vsftpd, list of essential packages, rabbitmq and mobile_connector for the odgassist software).
## Usage
0. Download.
0. Navigate into the ansible-java-deploy directory.
0. Fill variables in fabric.py like on example:
    ```
    env.guest_user = 'ubuntu'     # Remote user
    env.hosts = '192.168.50.11'   # Remote host
    env.ssh_key_dir = '~/.ssh'    # Ssh keys directory on local and remote hosts
    env.password = 'ubuntu'       # User password
    ```
0. Execute `fab bootstrap` and input user password if necessary.
0. Initially  "odgassist.yml" playbook is able to implement two snenarios: installs all packages or installs packages without rabbitmq with mobile_connector packages.
  Fill variables in inventory file like on the example:
    ```
    [without_rabbitmq]
    192.168.50.11
     
    [with_rabbitmq]
    192.168.50.11
     
    [all:vars]
    ansible_user=ubuntu
    ansible_ssh_private_key_file='~/.ssh/192.168.50.11_key'
     
    jenkins_output_folder='.'
    remote_mobile_connector_folder = '~/'
     
    postgresql_db_name='odgassist'
    postgresql_user='postgres'
    postgresql_pass='0000'
     
    [with_rabbitmq:vars]
    rabbitmq_user='mobile_scanner'
    rabbitmq_user_password='0000'
    rabbitmq_user2='process_scanner'
    rabbitmq_user2_password='0000'
    ```
0. Make necessary changes in deploy.sh for proper adjustment of "odgassist.yml" ansible playbook:
paste `--limit without_rabbitmq` to choose installation of all packages with rabbitmq + mobile_connector or 
paste `--limit with_rabbitmq` to install all. Example:
    ```
    ansible-playbook ./odgassist.yml --limit without_rabbitmq
    ```
    In order to install some particular packages use --skip-tags or --tags options. Detailed description is presented in the official documentation: 
    <http://docs.ansible.com/ansible/latest/playbooks_tags.html">
0. Execute `sh deploy.sh`.
