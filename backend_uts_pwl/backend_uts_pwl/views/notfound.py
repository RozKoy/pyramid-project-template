from pyramid.view import notfound_view_config


@notfound_view_config(renderer='backend_uts_pwl:templates/404.pt')
def notfound_view(request):
    request.response.status = 404
    return {}
