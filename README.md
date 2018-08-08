# Firefox Cookie Sweep

## The Problem
The internal settings for Firefox to clear cookies is limited. The particular use case that I was interested in was to clear cookies when the session closed, with some exceptions. For instance, clear all cookies except ones from my home server. Unfortunately, this logic is not available in Firefox.

## The Solution
Firefox stores all its cookies in a SQLite database in the user configuration. A script that will clear those cookies and allows exceptions based on domain name should fit my needs. Criteria could also be easily expanded to clear insecure cookies, third-party cookies or arbitrary expiry times.

## How to Use
Run the script (using Python 2) with the desired parameters whenever you see fit. On Linux, Windows and Mac it will be simplest to run the script as a shutdown or startup procedure. 

#### Clearing Cookies on Close
If you are on Linux, you could alter the Exec command of the Firefox desktop file (usually in `/usr/share/applications/`) to be `sh -c "firefox %u; python firefox-cookie-sweep <parameters>"` so that the script runs after Firefox terminates. However, note that this is not perfect and will result in cookies not being cleared if Firefox does not gracefully shutdown. Using this in combination with a startup/shutdown script is recommended.

#### Recommended Settings
In order to function properly, your Firefox settings need to be configured to not delete cookies. The relevant settings for this are under Preferences > Privacy & Security > Cookies and Site Data. Make sure that Firefox is set to accept cookies and site data from websites, and to keep them until they expire. Remember, Firefox Cookie Sweep will be manually deleting these as configured. Additionally, you might wish to have Firefox clear your history when it closes. In this case, make sure that Cookies is **not** selected in Privacy & Security > History > Settings.
