# Understanding FastAPI and Uvicorn

FastAPI and Uvicorn are a powerful duo used to build high-performance Python web applications, most commonly REST APIs.

## The Restaurant Analogy

An easy way to understand their relationship:

* 🍳 **FastAPI is the Chef:** Works in the kitchen—defining the menu, validating ingredients, and preparing the food (handling application logic, database routing, and data processing).
* 🤵 **Uvicorn is the Waiter:** Stands at the front of the restaurant—takes orders from customers, delivers them to the chef, and brings the finished meal back to the table (listening on the network port, receiving HTTP requests, and returning responses).

---

## What is FastAPI?

FastAPI is a modern, open-source Python web framework specifically designed for building APIs. It has become incredibly popular because it is fast to code and offers excellent performance.

### Key Features
* **Native Async Support:** Built from the ground up to support asynchronous programming (`async`/`await`), allowing it to handle thousands of concurrent requests efficiently.
* **Automatic Documentation:** Automatically generates interactive, browser-based API documentation (using Swagger UI and ReDoc) so you can test your endpoints instantly.
* **Data Validation:** Powered by Pydantic, it automatically checks incoming request data types and returns clear errors if something is incorrect.

---

## What is Uvicorn?

Uvicorn is a lightning-fast ASGI (*Asynchronous Server Gateway Interface*) web server. Because FastAPI does not include a built-in production web server, it relies on an external server program like Uvicorn to interact with the network.

### Key Features
* **ASGI Standard:** Unlike older WSGI servers (like Gunicorn or Flask's default server) which handle requests synchronously, ASGI allows for long-lived, asynchronous connections like WebSockets and HTTP/2.
* **Extreme Speed:** Built using highly optimized C-Python libraries like `uvloop` and `httptools`, making it one of the fastest web servers available for Python.

---

## How They Work Together

When running a FastAPI application, you typically start it using a terminal command like:

```bash
uvicorn main:app --reload
```

### Request Lifecycle

1. **Client Request:** A user sends a request to your application.
2. **Network Reception:** Uvicorn catches the request over the network and translates it into a Python-compatible format.
3. **ASGI Bridge:** Uvicorn passes the request to FastAPI using the ASGI protocol standard.
4. **App Execution:** FastAPI reads the request, validates the data, runs your custom Python code, and generates a response.
5. **Return Bridge:** FastAPI passes the response back to Uvicorn.
6. **Client Response:** Uvicorn sends the raw data back over the internet to the client's browser or client app.

## Checking the app
open by using http://127.0.0.1:8000/health
To see swager Docs http://127.0.0.1:8000/docs

curl -i http://localhost:8000/health

POST /triage-ticket

curl -i -X POST http://localhost:8000/triage-ticket \
  -H "Content-Type: application/json" \
  -d '{"ticket_text":"My package arrived damaged and I need help with a replacement."}'

  