from fastapi.openapi.docs import get_swagger_ui_html
from fastapi import FastAPI, applications
from routers import items, idCard, dbtest, qrCode
import os


def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url='https://cdn.bootcdn.net/ajax/libs/swagger-ui/4.10.3/swagger-ui-bundle.js',
        swagger_css_url='https://cdn.bootcdn.net/ajax/libs/swagger-ui/4.10.3/swagger-ui.css'
    )


applications.get_swagger_ui_html = swagger_monkey_patch
mode = os.environ.get('mode')

if mode == 'prod':
    app = FastAPI(openapi_prefix="/api/")
else:
    app = FastAPI()
app.include_router(items.router)
app.include_router(idCard.router)
app.include_router(dbtest.router)
app.include_router(qrCode.router)
