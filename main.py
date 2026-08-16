if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.presentation.api.app:app", reload=True)
