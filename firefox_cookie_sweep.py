import argparse

arg_parser = argparse.ArgumentParser(description='Clears Firefox cookies.')
arg_parser.add_argument('-d',
                        '--directory',
                        type=str,
                        help='The directory for your Firefox cookies. This can be found in Firefox at Help > Troubleshooting Information > Profile Directory',
                        required=True)
arg_parser.add_argument('-e',
                        '--except',
                        nargs='+',
                        type=str,
                        help='One or more domains which you do NOT want removed. Example: firefox_cookie_sweep.py --except aarondevelops.com google.com firefox.com')
                    
args = arg_parser.parse_args()