import cm_client
from cm_client.rest import ApiException
from pprint import pprint

# Authorisation
cm_client.configuration.username = 'admin'
cm_client.configuration.password = 'admin'

# Create an instance of the API class
api_host = 'http://pra-lzd-1.pra-lzd.root.hwx.site'
port = '7180'
api_version = 'v46'
# Construct base URL for API
# http://cmhost:7180/api/v30
api_url = api_host + ':' + port + '/api/' + api_version
api_client = cm_client.ApiClient(api_url)
cluster_api_instance = cm_client.ClustersResourceApi(api_client)

# Lists all known clusters.
api_response = cluster_api_instance.read_clusters(view='SUMMARY')
# print(api_response)
for cluster in api_response.items:
    print(cluster.name, "-", cluster.full_version)

# api_response2 = cluster_api_instance.read_clusters(view='EXPORT')
# print(api_response2.items)

api_response2 = cluster_api_instance.list_hosts('Cluster 1', view='SUMMARY')
# print(api_response2)
for host in api_response2.items:
    print(host.host_id,"-",host.host_url)
