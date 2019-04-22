import json
import re
import traceback

from common.constant import NETWORKS
from common.constant import GITHUB_NET_ID
from common.repository import Repository
from common.utils import Utils
from github_traffic import update_github_traffic

NETWORKS_NAME = dict((NETWORKS[netId]['name'], netId) for netId in NETWORKS.keys())
obj_util = Utils()
db = dict((netId, Repository(net_id=netId)) for netId in NETWORKS.keys())

def request_handler(event, context):
    print(event)
    try:
        net_id = GITHUB_NET_ID
        if db[net_id].connection is None:
            raise Exception('database connection is not initialized')
        update_github_traffic(repo=db[net_id])
        print("success")
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
    return