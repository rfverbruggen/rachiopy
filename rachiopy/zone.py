class Zone(object):
    def __init__(self, rachio):
        self.rachio = rachio

    def start(self, id, duration):
        url = '%szone/start' % self.rachio.server
        body = {'id': id, 'duration': duration}

        (resp, content) = self.rachio.h.request(url, 'PUT', body=body, headers=self.rachio.headers)
        return content

    def startMultiple(self, zones):
        url = '%szone/start_multiple' % self.rachio.server
        body = {'zones': zones}

        (resp, content) = self.rachio.h.request(url, 'PUT', headers=self.rachio.headers)
        return content

    def get(self, id):
        url = '%szone/%s' % (self.rachio.server, id)

        (resp, content) = self.rachio.h.request(url, 'GET', headers=self.rachio.headers)
        return content
