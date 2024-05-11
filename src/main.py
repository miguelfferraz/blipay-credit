"""Module for the HTTP server"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def _validate_params(self, params: dict, mandatory: list[tuple]) -> bool:
        """
        Validate if all mandatory parameters are provided and have the correct type.
        
        Args:
            params (dict): Query parameters
            mandatory (list[tuple]): List of tuples with the parameter and type

        Returns:
            bool: True if all parameters are valid, False otherwise            
        """
        for param, param_type in mandatory:
            if param not in params:
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                msg = f"400 Bad Request, missing parameter: {param}"
                self.wfile.write(bytes(msg, "utf8"))

                return False
            else:
                try:
                    # Validate type
                    _ = param_type(params[param][0])
                except ValueError:
                    self.send_response(400)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()

                    msg = f"400 Bad Request, invalid parameter type: {param}"
                    self.wfile.write(bytes(msg, "utf8"))

                    return False
        return True


    def do_GET(self):  # noqa N802
        parsed_url = urlparse(self.path)

        if parsed_url.path == "/score":
            query_params = parse_qs(parsed_url.query)
            mandatory_params = [
                ("name", str),
                ("age", int),
                ("income", int),
                ("city", str),
            ]

            if self._validate_params(query_params, mandatory_params):
                # TODO: Implement the score calculation
                pass
            else:
                return

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"404 Not Found")

def run(port=8080):
    http_server = HTTPServer(("", port), HTTPRequestHandler)
    
    print(f"Server started on port {port}")  # noqa T201
    http_server.serve_forever()


if __name__ == "__main__":
    run()