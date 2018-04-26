from django.http import JsonResponse
from rq import Queue
from worker import conn
from qtsp_solver.qtsp_subtree.src.forest_tsp_solver import ForestTSPSolver
import sys
import json
import numpy as np

def schedule_job(request):
    """
    :param request: HTTP request with following fields:
    - nodes: dictionary where keys correspond to node ids and values to coordinates.
    - first_node: integer - id of the first node
    :return:
    """
    request_dict = json.loads(request.read())
    print(request_dict)
    sys.stdout.flush()
    nodes = request_dict["nodes"]
    first_node = request_dict["first_node"]

    q = Queue(connection=conn)
    result = q.enqueue(
        solve_tsp, nodes, first_node)

    return JsonResponse({"status_code": 200})


def solve_tsp(nodes, first_node):
    forest_solver = ForestTSPSolver(np.array(nodes))
    forest_solution = forest_solver.solve_tsp()
    return forest_solution