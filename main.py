from fastapi import FastAPI

app = FastAPI(name="langgraph-ai-agent", version="0.1.0", description="A simple agent bot built with LangGraph AI.")

@app.get("/health")

async def health_check():
    return {"status": "ok"}



def main():
    print("Hello from agentbot!")


if __name__ == "__main__":
    main()
