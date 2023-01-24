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
    api_instance_core = kubernetes.client.CoreV1Api(api_client)

    try:
        api_response = api_instance.get_service_account_issuer_open_id_configuration()
        pprint(api_response)
        pprint("-------\n\n")
        ret = api_instance_core.list_pod_for_all_namespaces(watch=False)
        for pod in ret.items:
            print("%s\t%s\t%s" % (pod.status.pod_ip, pod.metadata.namespace, pod.metadata.name))
    except ApiException as e:
        print("Exception when calling WellKnownApi->get_service_account_issuer_open_id_configuration: %s\n" % e)
