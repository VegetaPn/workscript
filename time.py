from datetime import datetime
import sys

args = sys.argv

try:
    if len(args) == 1:
        args.append('now')

    if args[1] == 'now':
        datetime_now = datetime.now()
        sys.stdout.write(datetime_now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    elif len(args[1]) == 13:
        sys.stdout.write(datetime.fromtimestamp(int(args[1]) / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    elif len(args[1]) == 10:
        sys.stdout.write(datetime.fromtimestamp(int(args[1])).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    else:
        sys.stdout.write(str(int(datetime.strptime(args[1], '%Y-%m-%d %H:%M:%S').timestamp()) * 1000))
except Exception as e:
    sys.stdout.write('Error: ' + str(e))
