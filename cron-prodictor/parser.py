"""Create cron schedule from exported data from `crontab -l` ."""
from crontab import CronTab
from datetime import datetime
from datetime import timedelta
import os
import re
import warnings


IGNORE_CASE = ['MAILTO', '#']
CRON_FROM = datetime(2017, 1, 14, 23, 59, 59)
CRON_TO = datetime(2017, 1, 15, 6, 0, 0)
CRON_DIRECTORY_NAME = 'crontab'


def stop_future_warning(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', FutureWarning)
            func(*args, **kwargs)
    return wrapper


def __create_file_object_by_server():
    server_list = {}
    for server_file in os.listdir(CRON_DIRECTORY_NAME):
        file_path = os.path.join(CRON_DIRECTORY_NAME, server_file)
        f = open(file_path, 'r')
        lines = f.readlines()
        name, __ext = os.path.splitext(server_file)
        server_list[name] = lines
        f.close()
    return server_list


@stop_future_warning
def main():
    script_to_server = {}
    targets = {}

    for sv, lines in __create_file_object_by_server().items():
        for li in lines:
            li = li.replace('\n', '')
            if not is_cron_script(li):
                continue

            nz_crnon = normalize_cron_script(li)
            cron_time = nz_crnon[0]
            cron_script = nz_crnon[1]

            if cron_script in script_to_server:
                script_to_server[cron_script].append(sv)
            else:
                script_to_server[cron_script] = [sv]
            # TODO: has to handle error occuring missed cron script.
            c = CronTab(cron_time)

            current_time = CRON_FROM
            while current_time <= CRON_TO:
                interval_second = c.next(current_time)
                current_time = current_time + \
                    timedelta(seconds=interval_second)
                if current_time > CRON_TO:
                    break
                if current_time not in targets:
                    targets[current_time] = [cron_script]
                else:
                    targets[current_time].append(cron_script)
    export(targets, script_to_server)

def is_cron_script(cron_script):
    for c in IGNORE_CASE:
        if c in cron_script or cron_script == '':
            return False
    return True

def normalize_cron_script(cron_script):
    result = re.sub(r'  +', '\t', cron_script)
    result_list = result.split('\t')
    return (' '.join(result_list[0:5]), result_list[-1])

def export(targets, servers):
    with open('result.csv', 'w') as f:
        header = 'date, hour, miniute, second, scrip, server\n'
        f.write(header)
        for t, scripts in sorted(targets.items()):
            for s in scripts:
                server_name = ' or '.join(list(set(servers[s])))
                result = '{0},{1},{2}\n'.format(t.strftime('%Y-%m-%d,%H,%M,%S'),
                                                s,
                                                server_name)
                f.write(result)

if __name__ == '__main__':
    main()
