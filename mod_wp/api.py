from base import Configuration
import base64
import requests


class WpApi(Configuration):

    def __init__(self):
        Configuration.__init__(self)

        self.auth = self.get_configuration_for('authentication', 'parameter').encode()
        self.virtual_host = self.get_configuration_for('custom', 'virtual_host')
        self.request_headers = {"Authorization": 'Basic %s' % base64.b64encode(self.auth), "host": self.virtual_host}

    def request(self, resource=u'', parameters={}, http_method=u''):

        url = self.get_configuration_for('endpoint', 'url') + resource
        headers = self.request_headers

        if http_method == u'get':
            r = requests.get(url, headers=headers, params=parameters)
        elif http_method == u'post':
            r = requests.post(url, headers=headers, params=parameters)

        return {u'status_code': r.status_code, u'response_content': r.content, u'request_url': url}