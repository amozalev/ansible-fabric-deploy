#!/bin/bash
ansible-playbook ./odgassist.yml  --skip-tags "git, java, mobile_connector, nano, postgresql, rabbitmq, tomcat, vsftpd"