# ygetquote
Get Yahoo Financial Quotes using yours stored cookies (in mozilla format). The purpose is to use in Open Office Calc sheets.

Howto (Mac OSX):
 * Change yahoogetquote.py line 10 with the file path of yours cookies.txt (exported from your browser)
 * Put yahoogetquote.py into '/Users/uname/Library/Application Support/OpenOffice/4/user/Scripts/python', or equivalent if not OSx
 * Open the spreadsheet and go to Tools -> Macros -> Organize Macros -> Openoffice Basic
 * Under My Macros -> Standard, clique New
 * Put the content of openoffice_module.basic in the window opened (Open Office Basic), save and close the window
 * Call, in any sheet cell: =YAHOO_GETQUOTE("SYMBOL.SA") 
 * The SYMBOL.SA quote for 'now' should appear in the cell
