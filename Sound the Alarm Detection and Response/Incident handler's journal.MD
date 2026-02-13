# Incident Handler's Journal

## Journal Entry 1
**Date:** February 12, 2026

**Entry:** 001

**Description:** This entry documents the investigation of a brute-force login attempt detected on the corporate VPN gateway. The focus is on identifying the source and scope of the unauthorized access attempts to prevent a potential account takeover. [cite: 5]

**The 5 W's:** 
* **Who caused the incident?** An external threat actor using a botnet with rotating IP addresses.
* **What happened?** A high volume of failed login attempts was recorded against multiple employee accounts.
* **When did the incident occur?** The activity was flagged by the SIEM on February 11, starting at 22:00 UTC.
* **Where did the incident happen?** The attack targeted the primary external-facing VPN authentication portal.
* **Why did the incident happen?** The actor likely aimed to harvest valid credentials for future lateral movement within the network.

---

## Journal Entry 2
**Date:** February 13, 2026 

**Entry:** 002

**Description:** This entry details a security alert involving a suspicious file download on a workstation in the finance department. We are investigating whether the file contains malicious macros designed to execute code locally.

**The 5 W's:** 
* **Who caused the incident?** An employee inadvertently clicked a link in a phishing email disguised as an invoice.
* **What happened?** A macro-enabled spreadsheet was downloaded and attempted to establish an outbound connection.
* **When did the incident occur?** The download took place at 09:15 AM local time on February 13.
* **Where did the incident happen?** On a specific endpoint (Asset-ID: FIN-442) within the internal finance VLAN.
* **Why did the incident happen?** To install a remote access trojan (RAT) for financial data exfiltration.

---

## Journal Entry 3
**Date:** February 14, 2026

**Entry:** 003

**Description:** This entry outlines the application of network monitoring and packet analysis tools to identify anomalies in internal traffic. The goal was to verify the integrity of data transfers between the web server and the database. 

**Tool(s) used:**
* **Wireshark:** I used this tool to capture and interactively browse traffic running on the local network to inspect packet headers.
* **Tcpdump:** This command-line utility allowed for quick traffic capturing on the server-side without a graphical interface.
* **Snort:** I utilized this as an Intrusion Detection System (IDS) to automatically flag known malicious traffic patterns within the capture files.

---

## Journal Entry 4
**Date:** February 15, 2026

**Entry:** 004

**Description:** This entry focuses on using vulnerability scanning and reconnaissance tools to map the attack surface of a new development environment. This proactive measure ensures that no known vulnerabilities are exposed before the "go-live" date.

**Tool(s) used:** 
* **Nmap:** I performed network discovery and security auditing by scanning for open ports and identifying active services.
* **Nessus:** This tool was used to conduct a comprehensive vulnerability scan to find unpatched software and configuration errors.
* **Hashcat:** I used this tool in a controlled setting to test the strength of the system's password hashing algorithms against recovery attempts.

---

## Reflections/Notes

**Were there any specific activities that were challenging for you? Why or why not?**
The packet analysis activities using Wireshark were the most challenging because the sheer volume of network traffic was overwhelming at first. It required a deep understanding of protocols to filter out the "noise" and find the specific malicious packets.

**Has your understanding of incident detection and response changed since taking this course?**
My understanding has evolved from seeing it as a simple "fix-it" task to a highly structured, investigative process. I now appreciate how documenting the 5 W's ensures that the root cause is addressed rather than just the symptoms.

**Was there a specific tool or concept that you enjoyed the most? Why?**
I enjoyed using Nmap the most because of its versatility in uncovering what is actually happening on a network. It felt empowering to be able to map out an entire infrastructure and see the services running behind the scenes with just a few commands.