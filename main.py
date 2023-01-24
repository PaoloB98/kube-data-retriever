from __future__ import print_function
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

configuration = kubernetes.client.Configuration()
configuration.verify_ssl = False
# Configure API key authorization: BearerToken
configuration.api_key['Authorization'] = 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjEzdFdyMkdRTDZiVlIySnRwd2FiMmlUY0FiTTZMOEVtMTVVT2hEZ2VITjQifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4iLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjVmZDA1OGJkLWEyNzgtNDc2ZS1iYjA5LWU0MDFlZTYxMjM1NSIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.Jutbz-17yqZrtJL-cncY2g-7DKCkWzN3WaxHUBFqHW4ziiC_CPnujQ2wJw2YmLaVISUWyrBELjR_TY6xiAiYnzwQcYwSqoEkX2C8gAC67bjunbkVXXquvF21MPgW0PFuhznfV6XVsCCkYDT3bYmHWUIsutHRlumt71rD2z0OpD7eXxTv2PaXuHA269wNe___PZzaszUYNX7IMy3Qs-400GRkeT26_c7QE7L4m__YptLJ_tkzy3_uxdCUdAbfk_xv2GRPpT8po2YikxjpFn0BauYNUpAkDa2ijGijVOpbIO4BcWf4aQRfGS4XRuaegwwLFgInHt5IzMgbKfiEVu_1SA'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "https://192.168.13.76:6443"

# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes.client.WellKnownApi(api_client)

    try:
        api_response = api_instance.get_service_account_issuer_open_id_configuration()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WellKnownApi->get_service_account_issuer_open_id_configuration: %s\n" % e)
