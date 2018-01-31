# ansible-fabric-deploy
Generates ssh keys for remote host and installs a set of packages (git, java, Russian locale, nano, postgresql, 
tomcat, vsftpd, list of essential packages, rabbitmq and mobile_connector for the odgassist software).
## Requirements
Check that fabric and ansible are installed on your local machine.
## Usage
1. Clone or download.
0. Navigate into the directory.
0. Fill variables in fabric.py like on example:
    ```
    env.guest_user = 'ubuntu'     # Remote user
    env.hosts = '192.168.50.11'   # Remote host
    env.ssh_key_dir = '~/.ssh'    # Ssh keys directory on local and remote hosts
    env.password = 'ubuntu'       # User password
    ```
0. Fill variables in inventory file like on the example:
    ```
    192.168.50.11
 
    [all:vars]
    ansible_user=ubuntu
    ansible_ssh_private_key_file='~/.ssh/192.168.50.11_key'
    remote_user=ubuntu
     
    local_jenkins_output_folder='.'
    remote_project_folder = '/home/{{ remote_user }}/odgassist'
     
    odgassist_jar_file='lesha-1.0-SNAPSHOT-jar-with-dependencies.jar'
    mobile_connector_jar_file = 'mobile_connector-1.0-SNAPSHOT.jar'
     
    postgresql_db_name='odgassist'
    postgresql_db_port=5432
    postgresql_user='postgres'
    postgresql_pass='0000'
     
    allocated_memory = '-Xmx1G'
     
    mobile_connector_port=1234
    rabbitmq_user='user1'
    rabbitmq_user_password='0000'
    rabbitmq_user2='user2'
    rabbitmq_user2_password='0000'
    ```
0. Initial deploy.sh is intended to implement all tasks. Make necessary changes in deploy.sh in order to vary installation:
    use --skip-tags or --tags (equal to -t) options to remove or add packages to an installation.
    
    Example of installation of all packages without rabbitmq and mobile_connector:
    
    ```
    ansible-playbook ./odgassist.yml --skip-tags "rabbitmq,mobile_connector"
    ```
    
    Example of installation of java and tomcat:
    
    ```
    ansible-playbook ./odgassist.yml -t "java,tomcat"
    ```
    Detailed description is presented in the official documentation: 
    <http://docs.ansible.com/ansible/latest/playbooks_tags.html">
0. Execute `fab bootstrap` and input user password while needed. SSH keys are generated and installed on host machine.
0. Execute `sh deploy.sh`.
