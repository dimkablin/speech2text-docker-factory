"""uvicorn server running app."""
import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        host="127.0.0.1",
        port=8001,
        log_level="info",
        app="api.main:app",
        timeout_keep_alive=9999,
        ws_ping_timeout=9999,
        limit_concurrency=9999,
        reload=True,
        ssl_keyfile="ssl/local_key.pem",
        ssl_certfile="ssl/local_cert.pem"
    )
