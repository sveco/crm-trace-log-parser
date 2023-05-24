# crm-trace-log-parser
Python script to parse CRM server traces

If you [enable tracing](https://learn.microsoft.com/en-us/previous-versions/troubleshoot/dynamics/crm/how-to-enable-tracing-in-dynamics-crm) for On-Premise Dynamics 365 CE, generated files are not suitable to be imported for further analysis in Excel for example.
This Python script will parse all files in a folder and generate csv file from trace entry headers.

Remember to adjust path to folder containing trace logs.
