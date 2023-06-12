<p align="center">
    <img src="./docs/img/HoneyMonX.png"  width="256">
</p>

# HoneyMonX
HoneyMonX is a fully automated ICS/SCADA honeypot environment complete with a monitoring system intergrated. 
The honeypot is powered by the conpot honeypot develop by mushorg. the monitoring system is powered by WAZUH EDR.

<p align="center">
    <img src="./docs/img/SCADA-UI.png"  width="512">
</p>

the honeypot comes with a custom dummy Web UI as shown above. the values shown on the UI are source from known real values that were reseached for this particular purpose.

# Installation
before starting the installation process adjust the values that are found in the "playbooks/inventory.cfg". 
the values that are needed to be changes are the SSH credential (if key-auth is not enabled) and the IP address of the 2 machines.

To start the installation process run the following command on the root directory of the project:
```
# ansible-playbook playbooks/honeymonx-automation-master.yml
```
Alternatively if ssh key-auth is not enabled:
```
# ansible-playbook playbooks/honeymonx-automation-master.yml -kK
```

# Common Problem
Installation of Wazuh on Debian based system may faced "for apt not getting the lock it need" issued when running the playbook.
This issue normally caused by auto update features or an unattended upgrades.

To disable it and have the playbook run smoothly, you can turn the feature off by running the following on the Monitoring and Honeypot host:

```
--- select NO when prompted
# dpkg-reconfigure -plow unattended-upgrades
```

# How to contribute
If you want to contribute to this project start by making an issue ticket in the issue section, and then push your changes.

# Licences
This project is licences under GPL v2.0, if you dont have a copy, get one from here: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html