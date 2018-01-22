#!/bin/bash

ansible-playbook ./ansible/odgassist.yml\
--private-key=~/.ssh/192.168.50.11_key\
 -u ubuntu -i ./ansible/hosts\
  --tag=