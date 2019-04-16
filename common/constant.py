import os
IPFS_URL = {
    'url': 'ipfs.singularitynet.io',
    'port': '80',
    'protocol': 'http'
}
NETWORKS = {
    998: {
        'name': 'default',
		'db': {'DB_HOST': '127.0.0.1',
               'DB_USER': 'root',
               'DB_PASSWORD': 'root',
               'DB_NAME': 'local_snet_contract_index',
               'DB_PORT': 3306
               }
    }
}
MPE_EVTS = ['ChannelOpen', 'ChannelClaim', 'ChannelSenderClaim', 'ChannelExtend', 'ChannelAddFunds']
REG_EVTS = ['OrganizationCreated', 'OrganizationModified', 'OrganizationDeleted', 'ServiceCreated',
            'ServiceMetadataModified', 'ServiceTagsModified', 'ServiceDeleted']
COMMON_CNTRCT_PATH = './node_modules/singularitynet-platform-contracts'
REG_CNTRCT_PATH = COMMON_CNTRCT_PATH + '/abi/Registry.json'
MPE_CNTRCT_PATH = COMMON_CNTRCT_PATH + '/abi/MultiPartyEscrow.json'
REG_ADDR_PATH = COMMON_CNTRCT_PATH + '/networks/Registry.json'
MPE_ADDR_PATH = COMMON_CNTRCT_PATH + '/networks/MultiPartyEscrow.json'
SLACK_HOOK = {
    'hostname' : '',
    'port': 443,
    'path': '',
    'method': 'POST',
    'headers': {
        'Content-Type': 'application/json'
    }
}
ERROR_MSG = {
    1001: "Error Code: {} Network Id is Invalid !!",
    1002: "Error Code: {} Unable to process _init_w3.",
    9001: "Missing error code {} ",
    "default": "Unable to process error."
}
EVNTS_LIMIT = "100"
