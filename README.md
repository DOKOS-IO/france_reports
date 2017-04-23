## France Reports

This Frappe Application provides Specific Reports for France.
It is compatible with frappe framework 8.0 and above and ERPNext 8.0 and above.

It provides the following report:

 - Fichier des Ecritures Comptables [FEC]

### Fichier des Ecritures Comptables [FEC]
------------------------------------------
Since 2014, a legal requirement makes it mandatory for companies operating in France to provide a file of their general accounting postings by fiscal year corresponding to an electronic accounting journal.

For ERPNext users this file can be generated using the above report.

Use Instructions
----------------
>!!! THE CHART OF ACCOUNT MUST BE FORMATTED AS FOLLOWING: ACCOUNT NUMBER + "-" + ACCOUNT NAME (Example: "	701-Ventes de produits finis") !!!

 1. Generate the report and export it in .csv format (Menu > Export)
 2. Open in it Google Sheets or Libre Office and save it as tabular separated file (but keep the .csv extension)
 3. Rename the file as SIREN Number + FEC + Fiscal Year End Date (SirenFECYYYYMMDD)

Testing Instruction
-------------------
To test the validity of your file, the tax administration provides a testing tool at the following address:
[Outil de test des fichiers des écritures comptables (FEC)](http://www.economie.gouv.fr/dgfip/outil-test-des-fichiers-des-ecritures-comptables-fec)


#### License
------------

GPLv3