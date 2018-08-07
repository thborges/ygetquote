# ygetquote
Get Yahoo Financial Quotes using yours stored cookies (in mozilla format). The purpose is to use in Open Office Calc sheets.

Howto (Mac OSX):
 * Install an extension in your browser to export cookies in Mozilla format. cookies.txt works ok in Chrome: https://chrome.google.com/webstore/detail/cookiestxt/njabckikapfpffapmjgojcnbfjonfjfg
 * Login to your yahoo account and export the cookies for yahoo site
 * Change yahoogetquote.py line 10 with the file path of cookies.txt saved from previous step (exported from your browser)
 * Put yahoogetquote.py into '/Users/uname/Library/Application Support/OpenOffice/4/user/Scripts/python', or equivalent if not OSX (search for OpenOffice.org's user directory)
 * Check if the python macro was loaded in Openoffice, opening Tools -> Macros -> Organize Macros -> Python. It should appears as show in the image below:
 
   ![get_quotes loaded](https://github.com/thborges/ygetquote/raw/master/get_quote_loaded.png)
 
 * In a new/one spreadsheet, go to Tools -> Macros -> Organize Macros -> Openoffice Basic
 * Select My Macros -> Standard and clique New
 * Put the content of openoffice_module.basic file in the window opened (Open Office Basic), save and close the window
 * Put in any cell: =YAHOO_GETQUOTE("SYMBOL") 
 * The SYMBOL quote for today (default yahoo delay applies!) should appear in the cell. Examples:
 
   ![quote](https://github.com/thborges/ygetquote/raw/master/quotes.png)
