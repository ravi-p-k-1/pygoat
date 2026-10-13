import hashlib
import sqlite3

from django.http import JsonResponse


def cache_key(request):
    # MD5 only builds a short cache key here; it is not used for security.
    page = request.GET.get("page", "home")
    key = hashlib.md5(page.encode("utf-8")).hexdigest()
    return JsonResponse({"key": key})


def list_users(request):
    # Only one of two hard-coded column names can ever reach the query.
    order = "username" if request.GET.get("sort") == "name" else "id"
    conn = sqlite3.connect("db.sqlite3")
    rows = conn.execute(f"SELECT id, username FROM auth_user ORDER BY {order}").fetchall()
    return JsonResponse({"users": rows})
