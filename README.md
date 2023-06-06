<p align="center">
    <img src="./docs/img/HoneyMonX.png"  width="256">
</p>

# HoneyMonX
HoneyMonX is a fully automated ICS/SCADA honeypot environment complete with a monitoring system intergrated. The honeypot is powered by the conpot honeypot develop by mushorg.  

# Requirement

# Installation

# Common Problem
Installation of Wazuh on Debian based system may faced "for apt not getting the lock it need" issued when running the playbook.
This issue normally caused by auto update features or an unattended upgrades.

To turn disable it and have the playbook run smoothly, run the following on the Monitoring and Honeypot host:

```
--- select NO when prompted
# dpkg-reconfigure -plow unattended-upgrades
```


# How to contribute
