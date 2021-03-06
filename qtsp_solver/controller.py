from django.http import JsonResponse
from rq import Queue
from worker import conn
from qtsp_solver.qtsp_subtree.src.forest_tsp_solver import ForestTSPSolver
from qtsp_solver.qtsp_subtree.src.TSP_utilities import get_tsp_matrix
from qtsp_solver.models import TSPLog
import sys
import json
import numpy as np
import time

def schedule_job_with_nodes(request):
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
    distance_matrix = get_tsp_matrix(np.array(nodes))
    tol = 1e-2
    steps = 1
    if "tol" in request_dict.keys():
        tol = request_dict["tol"]
    if "steps" in request_dict.keys():
        steps = request_dict["steps"]
    current_log = TSPLog.objects.create(nodes=nodes, first_node=first_node, tol=tol, steps=steps)
    current_log.save()
    q = Queue(connection=conn)
    result = q.enqueue(
        solve_tsp, distance_matrix, first_node, steps, tol, current_log, timeout=3600)

    return JsonResponse({"status_code": 200, "id": current_log.id})

def schedule_job_with_distance_matrix(request):
    """
    :param request: HTTP request with following fields:
    - distance_matrix: dictionary where keys correspond to node ids and values to coordinates.
    - first_node: integer - id of the first node
    :return:
    """

    request_dict = json.loads(request.read())
    print(request_dict)
    sys.stdout.flush()
    distance_matrix = request_dict["distance_matrix"]
    first_node = request_dict["first_node"]
    tol = 1e-2
    steps = 1
    if "tol" in request_dict.keys():
        tol = request_dict["tol"]
    if "steps" in request_dict.keys():
        steps = request_dict["steps"]
    current_log = TSPLog.objects.create(nodes=None, distance_matrix=distance_matrix, first_node=first_node, tol=tol, steps=steps)
    current_log.save()
    q = Queue(connection=conn)
    result = q.enqueue(
        solve_tsp, distance_matrix, first_node, steps, tol, current_log, timeout=3600)

    return JsonResponse({"status_code": 200, "id": current_log.id})



def solve_tsp(distance_matrix, first_node, steps, tol, current_log):
    start_time = time.time()

    forest_solver = ForestTSPSolver(np.array(distance_matrix), steps=steps, ftol=tol, xtol=tol)
    forest_solution, forest_distribution = forest_solver.solve_tsp()
    distribution = {}
    for order_tuple, count in forest_distribution.items():
        new_key = " ".join(map(str,order_tuple))
        distribution[new_key] = count

    end_time = time.time()
    processing_time = int(end_time - start_time)
    current_log.processing_time = processing_time
    current_log.solution = forest_solution
    current_log.distribution = json.dumps(distribution)
    current_log.save()


def get_result(request):
    request_dict = json.loads(request.read())
    result_id = request_dict["id"]
    result_log = TSPLog.objects.filter(id=result_id)[0]
    solution = result_log.solution
    processing_time = result_log.processing_time
    distribution = result_log.distribution
    return JsonResponse({"solution":solution, "processing_time":processing_time, "distribution":distribution})


