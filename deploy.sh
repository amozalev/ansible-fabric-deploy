#!/bin/bash
ansible-playbook ./odgassist.yml --skip-tags "git,rabbitmq" -t "mobile_connector"