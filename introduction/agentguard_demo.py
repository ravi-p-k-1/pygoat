import base64
import pickle
import sqlite3
import subprocess

from django.http import HttpResponse


def ping_host(request):
    host = request.GET.get("host", "")
    output = subprocess.check_output("ping -c 1 " + host, shell=True)
    return HttpResponse(output)


def find_user(request):
    name = request.GET.get("name", "")
    conn = sqlite3.connect("db.sqlite3")
    rows = conn.execute("SELECT * FROM auth_user WHERE username = '%s'" % name).fetchall()
    return HttpResponse(str(rows))


def load_prefs(request):
    data = base64.b64decode(request.COOKIES.get("prefs", ""))
    return HttpResponse(str(pickle.loads(data)))
