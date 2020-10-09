from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from webapp_workflow_automator.rest_api import WebappAutomatorAPI

app = FastAPI(debug=True)


def get_application() -> FastAPI:
    application = FastAPI(title="Image Getter",
                          description="App to get images from Browser via REST API", version="0.0.1")
    origins = ["*"]
    # application.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=origins,
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )
    # application.include_router(processA.router)
    return application


app = get_application()


@app.get("/", response_class=HTMLResponse)
async def browse(q: str = 'apple'):
    """
    Google search image results for a given query.

    :param q: str

    :return: None
    """

    w = WebappAutomatorAPI()
    img = w.search(query=q)
    w.close()

    return f"""
    <html>
        <body>
            First result from the search:
            <br/>
            <img src='{img}'></img>
        </body>
    </html>
    """
