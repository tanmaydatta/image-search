from django.shortcuts import render
from django.http import *
import json
from image_module import *
from django.views.decorators.csrf import *
from models import *
import ipdb

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
	rows = request.GET.get("rows", 6)
	res = get(query, page, rows)
	return render(request, "results.html", {"res": res, "query": query, "page": page})

@csrf_exempt
def add(request):
	if request.method != "POST":
		return response("failed", "POST required")
	url = request.POST.get("url", "")
	callback = request.POST.get("callback", "/search")
	if not url:
		return response("failed", "url not entered")
	name = url.split("/")[-1]
	img = Image(name=name, url=url)
	try:
		img.create()
	except Exception as e:
		return response("failed", "exception occured", exception=str(e))
	return HttpResponseRedirect(callback)
