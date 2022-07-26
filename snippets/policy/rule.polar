allow(_user: User, "GET", http_request: HttpRequest) if
    http_request.path = "/test-oso/";
