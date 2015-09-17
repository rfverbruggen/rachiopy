import json

class Zone(object):
    def __init__(self, rachio):
        self.rachio = rachio

    def start(self, id, duration):
        url = '%szone/start' % self.rachio.server
        payload = {'id': id, 'duration': duration}

        (resp, content) = self.rachio.h.request(url, 'PUT', body=json.dumps(payload), headers=self.rachio.headers)
        return (resp, content)

    def startMultiple(self, zones):
        url = '%szone/start_multiple' % self.rachio.server
        payload = {'zones': zones}

        (resp, content) = self.rachio.h.request(url, 'PUT', body=json.dumps(payload), headers=self.rachio.headers)
        return (resp, content)

    def get(self, id):
        url = '%szone/%s' % (self.rachio.server, id)

        (resp, content) = self.rachio.h.request(url, 'GET', headers=self.rachio.headers)
        return (resp, content)
