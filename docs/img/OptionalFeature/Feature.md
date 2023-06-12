# Monitoring pfSense with Wazuh

This is optional feature that could be implement easily together with the whole conpot environment. Certainly, you would need to Wazuh and pfSense firewall in order to be able to monitor the firewall.  You will not find many tutorials about this kind of thing, so this could be quite useful and you can play with it.

The first step towards this is to allow pkg to pull from the repository, and we need to configure a couple of files. The files that should be edited are "pfSense.conf" and "FreeBSD.conf" and you basically need to check whether the first line about FreeBSD is set to "yes."
Following installation of the agent, you'll see some output on configuring your agent. Then we continue with couple of steps that are needed copying files and adding the IP of wazuh manager in the “ossec.conf”

Then we need to start the Wazuh agent and enable start at boot with these commands. 
1.	`sysrc wazuh_agent_enable="YES" `
2.	`ln -s /usr/local/etc/rc.d/wazuh-agent /usr/local/etc/rc.d/wazuh-agent.sh `
3.	`service wazuh_agent start`

Next big step is to have Suricata installed on the pfSense and in every single interface to have check on EVE JSON LOG and the EVE Output type should be FILE.

Going into the next big steps, here you go to the wazuh dashboard and create a new group (for example called pfSense). Add the following lines to the group shared configuration.
Once you save it, the Wazuh manager will push the changes to any member(s) of the group.
```xml
<localfile>
        <logs_format>json</log_format>
        <location>/var/log/suricata/*/eve.json</location>
</localfile>
```

The last big step is to create the rules in the wazuh in order to receive alerts. pfSense has the decoders and rules in place to monitor the output in /var/log/filter.log. 
Decoders tell the Wazuh manager how to process the lines of the log output. 
Before adding the rules for wazuh, we need to to have the Wazuh agent monitor the pfSense firewall log, just add another directive to the agent.conf file like we did with the eve.json logs before. We need to go the configuration group that we created earlier in my case the name is pfSense and add this piece of configuration.
```xml
<localfile>
        <logs_format>syslog</log_format>
        <location>/var/log/filter.log</location>
</localfile>
```

Finally, you can create a new rule file and there to put the exact rule that will trigger alerting. The following rule is used:

```xml
<group name="pfsense,">
  <rule id="87701" level="5" overwrite="yes">
    <if_sid>87700</if_sid>
    <action>block</action>
    <options>no_log</options>
    <description>pfSense firewall drop event.</description>
    <group>firewall_block,pci_dss_1.4,gpg13_4.12,hipaa_164.312.a.1,nist_800_53_SC.7,tsc_CC6.7,tsc_CC6.8,</group>
  </rule>
 </group>
```
