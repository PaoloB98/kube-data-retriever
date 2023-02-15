from __future__ import print_function

import json
from typing import List

import kubernetes.client
import yaml
from kubernetes.client import Configuration
from kubernetes.client.rest import ApiException
from kubernetes import config
from pprint import pprint
from models import UndetailedBlueprint
import requests

CONFIG_FILE: str = "./secrets/config"

client_config = type.__call__(Configuration)
config.load_kube_config(config_file=CONFIG_FILE, context=None, client_configuration=client_config, persist_config=False)
client_config.verify_ssl = False


def load_configuration() -> dict:
    with open(".config", 'r') as stream:
        conf = None
        try:
            conf = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
        return conf

def get_all_pods():
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

def get_blueprints(nfvcl_conf: dict) -> List[UndetailedBlueprint]:
    blue_list: List[UndetailedBlueprint] = []
    port = nfvcl_conf['port']
    ip = nfvcl_conf['ip']
    response = requests.get("http://{}:{}/nfvcl/v1/api/blue/".format(ip,port))
    parsed_json = json.loads(response.text)
    for blueprint in parsed_json:
        blue_model_instance = UndetailedBlueprint.parse_obj(blueprint)
        blue_list.append(blue_model_instance)
    return blue_list

configuration = load_configuration()

#get_all_pods()

get_blueprints(configuration['nfvcl'])