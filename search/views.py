from django.shortcuts import render
from django.http import *
import json
from image_module import *

# Create your views here.
def response(status, msg, *args):
	# args are tuples
	res = {}
	res['status'] = status
	res['msg'] = msg
	for arg in args:
		res[arg[0]] = arg[1]
	return HttpResponse(json.dumps(res))

def home(request):
	return render(request, "search.html")

def results(request):
	query = request.GET.get("query")
	page = request.GET.get("page", 0)
	rows = request.GET.get("rows", 5)
	res = get(query, page, rows)
	return render(request, "results.html", {"res": res, "query": query, "page": page})