#!/bin/bash
ansible-playbook ./odgassist.yml --skip-tags "tomcat,java,git,mobile_connector,postgresql,rabbitmq"