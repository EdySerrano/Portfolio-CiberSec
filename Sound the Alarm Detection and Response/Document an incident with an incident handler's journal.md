# Incident Handler's Journal

| Field | Details |
| :--- | :--- |
| **Date** | February 9, 2026 |
| **Entry** | 1 |
| **Description** | Initial documentation of a ransomware attack resulting in the encryption of critical medical records and a complete shutdown of business operations at a U.S. healthcare clinic. |
| **Tool(s) used** | Email Security Gateway (to analyze phishing headers), Antivirus/Endpoint Detection and Response (EDR), Backup Management Software, and Network Traffic Analysis tools. |

## The 5 W's

**Who caused the incident?**
The incident was caused by an organized group of unethical hackers known for targeting organizations within the healthcare and transportation industries.

**What happened?**
The attackers sent targeted phishing emails with malicious attachments that, once downloaded, deployed ransomware. This malware encrypted critical patient data and business software, leading to a total operational shutdown and a demand for a ransom payment in exchange for a decryption key.

**When did the incident occur?**
The security incident occurred on a Tuesday morning at approximately 9:00 a.m.

**Where did the incident happen?**
The incident took place at a small primary-care health clinic located in the United States.

**Why did the incident happen?**
The incident occurred because employees downloaded a malicious attachment from a phishing email, providing the attackers access to the network. The hackers' ultimate goal was to extort a large sum of money from the clinic in exchange for restoring access to encrypted files.

## Additional Notes
I need to determine if the clinic's data backup policy includes "off-site" or "immutable" backups to see if recovery is possible without paying the ransom. Additionally, I should investigate whether any Protected Health Information (PHI) was exfiltrated (stolen) before the encryption took place, as this would trigger legal reporting requirements under HIPAA.