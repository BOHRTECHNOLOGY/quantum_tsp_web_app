from django.shortcuts import render
from django.http import HttpResponse

from .qtsp_subtree.src.forest_tsp_solver import ForestTSPSolver
import numpy as np
from .models import Greeting

import requests

# Create your views here.
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    nodes_array = np.array([[0, 0], [1, 1]])
    tsp_solver = ForestTSPSolver(nodes_array, steps=1, ftol=1e-2, xtol=1e-2)
    tsp_solver.solve_tsp()
    results = tsp_solver.get_solution()
    line_1 = "Nodes coordinates" + str(nodes_array)
    line_2 = "Results:" + str(results)
    print("FINISHED!")
    print("RESULTS:", results)
    return HttpResponse('<pre>' + line_1 + "\n" + line_2 + '</pre>')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

