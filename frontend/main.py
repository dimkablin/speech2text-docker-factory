"""uvicorn server running app."""
from gradio_app import iface

if __name__=="__main__":
    iface.launch(
        server_name="0.0.0.0", 
        server_port=8001,
        ssl_certfile="ssl/local_cert.pem",
        ssl_keyfile="ssl/local_key.pem",
        ssl_verify=False
    )
