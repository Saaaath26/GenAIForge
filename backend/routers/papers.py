from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()


@router.get("/search")
async def search_papers(query: str):

    url = "https://api.semanticscholar.org/graph/v1/paper/search"

    headers = {
        "User-Agent": "GenAIForge/1.0"
    }

    params = {
        "query": query,
        "limit": 5,
        "fields": "title,abstract"
    }

    try:
        response = requests.get(url, params=params, headers=headers)

        print("STATUS:", response.status_code)
        print("TEXT:", response.text)

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.text
            )

        data = response.json()

        papers = []

        for paper in data.get("data", []):
            papers.append({
                "title": paper.get("title"),
                "abstract": paper.get("abstract")
            })

        return {"papers": papers}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))