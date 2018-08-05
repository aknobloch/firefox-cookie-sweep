# Firefox Cookie Sweep

## The Problem
The internal settings for Firefox to clear cookies is limited. The particular use case that I was interested in was to clear cookies when the session closed, with some exceptions. For instance, clear all cookies except ones from my home server. Unfortunately, this logic is not available in Firefox.

## The Solution
Firefox stores all its cookies in a SQLite database in the user configuration. A script that will clear those cookies and allows exceptions based on domain name should fit my needs. Criteria could also be easily expanded to clear insecure cookies, third-party cookies or arbitrary expiry times.

## How to Use
Run the script with the desired parameters whenever you see fit. On Linux, Windows and Mac it will be simplest to run the script as a shutdown or startup procedure. If you are on Linux, you could alter the start command of Firefox to be `firefox && firefox-cookie-sweep <parameters>` so that the script runs after Firefox terminates. 
