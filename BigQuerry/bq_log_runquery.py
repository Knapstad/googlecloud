import time
from google.protobuf.timestamp_pb2 import Timestamp 
from google.cloud import bigquery_datatransfer_v1

def runQuery ():
    client = bigquery_datatransfer_v1.DataTransferServiceClient()
    project_id = '675381473435'
    config_id = '61636307-0000-29a9-8102-d4f547eb0e78'
    location_id = 'europe'
    response = client.start_manual_transfer_runs(
        request={
            "parent": f"projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}",
            "requested_run_time": Timestamp(seconds=int(time.time()), nanos=0),
        }
        )
    print(response)