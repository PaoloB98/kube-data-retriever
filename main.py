from __future__ import print_function
import kubernetes.client
from kubernetes.client import Configuration
from kubernetes.client.rest import ApiException
from kubernetes import config
from pprint import pprint

CONFIG_FILE: str = "./secrets/admin.conf"

client_config = type.__call__(Configuration)
config.load_kube_config(config_file=CONFIG_FILE, context=None, client_configuration=client_config, persist_config=False)
client_config.verify_ssl = False

# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(client_config) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes.client.WellKnownApi(api_client)

    try:
        api_response = api_instance.get_service_account_issuer_open_id_configuration()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WellKnownApi->get_service_account_issuer_open_id_configuration: %s\n" % e)
