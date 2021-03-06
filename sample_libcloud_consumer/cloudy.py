import os, sys
import libcloud
from libcloud.storage.types import Provider
from libcloud.storage.providers import get_driver

libcloud.enable_debug(sys.stdout)

class Cloudy(object):
    def cloudy(self):
        S3_ACCESS_ID = os.getenv('AWS_ACCESS_KEY_ID')
        S3_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

        Driver = get_driver(Provider.S3)
        conn = Driver(S3_ACCESS_ID, S3_SECRET_KEY)

        containers = conn.list_containers()
        print('%d containers:' % len(containers))
        for container in containers:
            print(' - %s' % container.name)

if __name__ == '__main__':
    Cloudy().cloudy()
