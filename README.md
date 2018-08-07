# ygetquote
Get Yahoo Financial Quotes using yours stored cookies (in mozilla format). The purpose is to use in Open Office Calc sheets.

Howto (Mac OSX):
 * Change yahoogetquote.py line 10 with the file path of yours cookies.txt (exported from your browser)
 * Put yahoogetquote.py into '/Users/uname/Library/Application Support/OpenOffice/4/user/Scripts/python', or equivalent if not OSx
 * Check if the python macro was loaded opening Tools -> Macros -> Organize Macros -> Python. It should appears as show in the image below:
   ![get_quotes loaded](https://github.com/thborges/ygetquote/raw/master/get_quote_loaded.png)
 
 * Open a new/one spreadsheet and go to Tools -> Macros -> Organize Macros -> Openoffice Basic
 * Select My Macros -> Standard and clique New
 * Put the content of openoffice_module.basic file in the window opened (Open Office Basic), save and close the window
 * Put in any cell: =YAHOO_GETQUOTE("SYMBOL.SA") 
 * The SYMBOL.SA quote for 'now' should appear in the cell
