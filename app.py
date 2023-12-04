import waitress

# class App():
#     def __call__(self):
#         pass


def app(environ, start_response):
    data = b"<h1>Bonjour!</h1>"
    status = "200 OK"
    headers = [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(data))),
        ("Formation", "M2i"),
    ]

    start_response(status, headers)
    return iter([data])


waitress.serve(app, listen="127.0.0.1:8000")
