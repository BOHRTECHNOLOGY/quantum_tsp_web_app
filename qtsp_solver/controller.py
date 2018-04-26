from django.http import JsonResponse


def schedule_job(request):
    """

    :param request: HTTP request with following fields:
    - nodes: dictionary where keys correspond to node ids and values to coordinates.
    - first_node: integer - id of the first node
    :return:
    """
    return JsonResponse({"status_code": 200})
