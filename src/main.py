"""Module for the HTTP server"""

import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from src.logger import logger
from src.creditscore import CreditScoreCalculator

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

                msg = f"Missing parameter: {param}"
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

                    msg = f"Invalid type for parameter: {param}, expected {param_type.__name__}"
                    self.wfile.write(bytes(msg, "utf8"))

                    return False
        return True
    
    def _process_score_consult(self, query_params: dict):
        """
        Process the score consult request.

        Args:
            query_params (dict): Query parameters
        """
        mandatory_params = [
            ("name", str),
            ("age", int),
            ("income", int),
            ("city", str),
        ]

        if not self._validate_params(query_params, mandatory_params):
            return
        
        try:
            calculator = CreditScoreCalculator(
                name=query_params["name"][0],
                age=int(query_params["age"][0]),
                income=int(query_params["income"][0]),
                city=query_params["city"][0],
            )

            _, msg = calculator.has_approved_credit()
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(str(e), "utf8"))
            
            return

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(msg, "utf8"))

    def do_GET(self):  # noqa N802
        parsed_url = urlparse(self.path)

        if parsed_url.path == "/score":
            query_params = parse_qs(parsed_url.query)
            self._process_score_consult(query_params=query_params)
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"404 Not Found")

        return


def run(port=8080):
    http_server = HTTPServer(("", port), HTTPRequestHandler)

    logger.info(f"Server started on port {port}...")
    http_server.serve_forever()


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--port", type=int, default=8080)

    args = argparser.parse_args()
    run(args.port)
