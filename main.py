from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

app = FastAPI()

app.mount("/", StaticFiles(directory="client/public", html=True), name="client")
app.mount("/build", StaticFiles(directory="client/public/build"), name="build")

@app.get('/{full_path:path}')
async def front():
   return RedirectResponse(url='/')