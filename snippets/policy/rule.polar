
allow(_user: User, "GET", http_request: rest_framework::request::Request) if
    http_request.path = "/test-oso";