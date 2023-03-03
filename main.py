from __future__ import print_function

import json
from typing import List
import kubernetes.client
import yaml
from kubernetes.client import Configuration, V1PodList, V1PodStatus, V1Pod
from kubernetes.client.rest import ApiException
from kubernetes import config
from pprint import pprint
from models import UndetailedBlueprint, K8sCluster
import requests

CONFIG_FILE: str = "./secrets/viewer.conf"

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


def get_pods_for_namespace(kube_client_config: Configuration,) -> V1PodList:
    """
    @:rtype V1PodList:
    :return: Return the list of pods of the k8s controller specified in configuration files
    """

    # Enter a context with an instance of the API kubernetes.client
    with kubernetes.client.ApiClient(kube_client_config) as api_client:
        # Create an instance of the API class
        api_instance = kubernetes.client.WellKnownApi(api_client)
        api_instance_core = kubernetes.client.CoreV1Api(api_client)
        pod_list: V1PodList = None

        try:
            api_response = api_instance.get_service_account_issuer_open_id_configuration()
            pprint(api_response)
            pprint("-------\n\n")
            pod_list = api_instance_core.list_pod_for_all_namespaces(watch=False)
            pod: V1Pod
            for pod in pod_list.items:
                print("%s\t%s\t%s\t%s" % (pod.status.pod_ip, pod.metadata.namespace, pod.metadata.name, pod.status.container_statuses[0].container_id))
        except ApiException as e:
            print("Exception when calling WellKnownApi->get_service_account_issuer_open_id_configuration: %s\n" % e)
        return pod_list


def get_blueprints(nfvcl_conf: dict) -> List[UndetailedBlueprint]:
    blue_list: List[UndetailedBlueprint] = []
    port = nfvcl_conf['port']
    ip = nfvcl_conf['ip']
    response = requests.get("http://{}:{}/nfvcl/v1/api/blue/".format(ip, port))
    parsed_json = json.loads(response.text)
    for blueprint in parsed_json:
        blue_model_instance = UndetailedBlueprint.parse_obj(blueprint)
        blue_list.append(blue_model_instance)
    return blue_list


def get_k8s_cluster(nfvcl_conf: dict):
    k8s_cluster_list: List[UndetailedBlueprint] = []
    port = nfvcl_conf['port']
    ip = nfvcl_conf['ip']
    response = requests.get("http://{}:{}/v1/topology/kubernetes".format(ip, port))
    parsed_json = json.loads(response.text)
    for k8s_clust in parsed_json:
        k8s_cluster_instance = K8sCluster.parse_obj(k8s_clust)
        k8s_cluster_list.append(k8s_cluster_instance)
    return k8s_cluster_list


configuration = load_configuration()
get_pods_for_namespace(client_config)





#kube_conf = Configuration(host="https://192.168.17.28/k8s/clusters/c-m-7glfvxrv", api_key="kubeconfig-user-nfn45svckx:zpnkjblcc5f7b7ppk5k22phhrghrkzt2l4tkqbxnh8bpgpkxwh4h9l")
#kube_conf.verify_ssl = False

# get_all_pods()

#instantiated_blueprint_list = get_blueprints(configuration['nfvcl'])
#k8s_cluster_list = get_k8s_cluster(configuration['nfvcl'])
