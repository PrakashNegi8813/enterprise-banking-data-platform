import uuid
from datetime import datetime


def create_context(dataset):

    return {

        "batch_id": str(uuid.uuid4()),

        "dataset": dataset,

        "pipeline_name": "Enterprise Banking Pipeline",

        "start_time": datetime.now()

    }