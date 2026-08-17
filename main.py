import os

from cloudlink import server
from cloudlink.server.protocols import clpv4, scratch

if __name__ == "__main__":
    # Instantiate the server object
    server = server()

    # Set logging level.
    # INFO keeps things quiet; change to server.logging.DEBUG if you need to
    # see every message the server handles while troubleshooting.
    server.logging.basicConfig(level=server.logging.INFO)

    # Load protocols (CL4 + Scratch cloud variables)
    clpv4 = clpv4(server)
    scratch = scratch(server)

    # Start the server!
    # Render assigns a port via the PORT environment variable, and requires
    # binding to 0.0.0.0 (not 127.0.0.1) so it's reachable from outside.
    server.run(ip="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
