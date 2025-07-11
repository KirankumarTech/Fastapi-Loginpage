from fastapi import FastAPI
from auth_routes import auth_router
from fastapi_jwt_auth import AuthJWT
from schemas import Settings
from fastapi.routing import APIRoute
from fastapi.openapi.utils import get_openapi
import inspect, re

app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Login API",
        version="1.0",
        description="An API for a login Service",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "Bearer Auth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Enter: **'Bearer &lt;JWT&gt;'**, where JWT is the access token"
        }
    }

    api_routes = [route for route in app.routes if isinstance(route, APIRoute)]

    for route in api_routes:
        path = getattr(route, "path")
        endpoint = getattr(route, "endpoint")
        methods = [method.lower() for method in getattr(route, "methods")]

        for method in methods:
            if re.search("jwt_required|fresh_jwt_required|jwt_optional", inspect.getsource(endpoint)):
                openapi_schema["paths"][path][method]["security"] = [{"Bearer Auth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@AuthJWT.load_config
def get_config():
    return Settings()


app.include_router(auth_router)
