import os
import datetime
import requests


def fetch_remote_file(url, cache = '', expire = 0):

    if cache and expire:

        expire = (datetime.datetime.now() - datetime.timedelta(minutes=expire)).strftime('%s')

        if not os.path.isfile(cache) or int(os.path.getmtime(cache)) < int(expire):

            try:

                content = requests.get(url, verify=False).text.encode('utf-8')
                file_put_contents(cache, content)

            except Exception, e:
                print e

        else:

            content = file_get_contents(cache)

    else:

        content = requests.get(url, verify=False).text.encode('utf-8')

    return content


def file_get_contents(file):

    if os.path.isfile(file):

        file = open(file, 'r')
        content = file.read()
        file.close()

        return content


def file_put_contents(file, content):

    file = open(file, 'w')
    file.write(content)
    file.close()

    return content
