#!/bin/bash

ansible-playbook ./ansible/odgassist.yml --private-key=~/.ssh/id_rsa -u deployer -i ./ansible/hosts --tag=