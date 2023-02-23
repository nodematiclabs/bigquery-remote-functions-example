import functions_framework

from google.cloud import bigquery

import pydp as dp
from pydp.algorithms.laplacian import BoundedMean

client = bigquery.Client()
bounded_mean = BoundedMean(epsilon=0.9, lower_bound=0.0, upper_bound=5000.0, dtype="float")

@functions_framework.http
def entrypoint(request):
    request_json = request.get_json(silent=True)

    if request_json and 'calls' in request_json:
        results = []
        for call in request_json['calls']:
            results.append(
                round(bounded_mean.quick_result(call[0]))
            )
        return {'replies': results}
    else:
        return ""