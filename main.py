from fanstatic import FastAPT
from fastapi.templating import Jinja2Templates


app = FastAPT()
templates = Jinja2Templates(directory="templates")


@app.route("/")
def readme():
    return {
        "data": "Hello World"
        }
    @app.get("tomato")
    def tomato():
        return templates.TemplateResponse("index.html")           
