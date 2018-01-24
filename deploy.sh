#!/bin/bash
ansible-playbook ./odgassist.yml --skip-tags "git,rabbitmq" -t "nano"