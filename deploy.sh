#!/bin/bash
ansible-playbook ./odgassist.yml --tags="packages,nano,locales,java,nginx,postgresql,odgassist,supervisor"
