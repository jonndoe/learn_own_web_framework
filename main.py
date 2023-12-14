def application(environ, start_response):
    response_body = [f"{key}: {value}" for key, value in sorted(environ.items())]
    response_body = "\n".join(response_body)
