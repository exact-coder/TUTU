import os


class Graphset(object):
    pass


class Uptime(Graphset):
    def poll(self, tick):
        pass


class SystemLoad(Graphset):
    def poll(self, tick):
        return os.getloadavg()[0]
