from mod_wp.transform import Data


def main():

    d = Data()

    # Example (1) List all the published WordPress pages - i.e. does not include drafts etc.
    data = d.transform_request_response_to_python_data_structure(resource='/pages', parameters={}, http_method=u'get')

    # Example (2) List all the published WordPress posts - i.e. does not include drafts etc.
    data = d.transform_request_response_to_python_data_structure(resource='/posts', parameters={}, http_method=u'get')


if __name__ == "__main__":
    main()