from django.shortcuts import render
from django.http import HttpResponse

from .qtsp_subtree.src.forest_tsp_solver import ForestTSPSolver
import numpy as np

# Create your views here.
def index(request):
    nodes_array = np.array([[0, 0], [1, 1]])
    tsp_solver = ForestTSPSolver(nodes_array, steps=1, ftol=1e-2, xtol=1e-2)
    results, distribution = tsp_solver.solve_tsp()
    line_1 = "Nodes coordinates" + str(nodes_array)
    line_2 = "Results:" + str(results)
    line_3 = "Distribution:" + str(distribution)
    print("FINISHED!")
    print("RESULTS:", results)
    return HttpResponse('<pre>' + line_1 + "\n" + line_2 + "\n" + line_3 + '</pre>')
