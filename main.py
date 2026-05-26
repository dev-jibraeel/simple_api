from fastapi import FastAPI

hadees = {"hadees": "انما الاعمال بالنيات، و انما لكل امري ما نوي"}

app = FastAPI()


@app.get("/")
def index():
    return {"book": "riyalus saaliheen", "only_hadees": hadees["hadees"]}
