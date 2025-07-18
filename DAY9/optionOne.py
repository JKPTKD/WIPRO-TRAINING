import argparse
import os
from datetime import datetime
parser = argparse.ArgumentParser(description="Process some options.")
parser.add_argument("-l", "--list", action="store_true", help="List files in current directory")
parser.add_argument("-d", "--date", action="store_true", help="Show today's date")
parser.add_argument("-e", "--echo", type=str, help="Display the given string")
args = parser.parse_args()
if args.list:
    print("Listing files in current directory:")
    os.system("dir" if os.name == 'nt' else "ls")
if args.date:
    print("Today's date is:", datetime.now().strftime("%Y-%m-%d"))
if args.echo:
    print("Echoed string:", args.echo)
