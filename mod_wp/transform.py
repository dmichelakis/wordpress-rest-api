from mod_wp.api import WpApi as api
import json


class Data(api):

    def __init__(self):
        api.__init__(self)

    def transform_request_response_to_python_data_structure(self, resource=u'', parameters={}, http_method=u''):
        """
        Returns a list of dictionaries which represent the content response from a request
        :param resource:
        :param parameters:
        :return:
        """

        data = self.request(resource, parameters, http_method)
        print(data)

        if data[u'status_code'] is 200:
            return json.loads(data[u'response_content'])
        else:
            return []
