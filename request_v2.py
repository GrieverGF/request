from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("NgrokFetcher")

@mcp.tool()
def fetch_ngrok_endpoint(path: str = "") -> str:
    """Consulta el endpoint ngrok configurado pasando el bypass del interstitial."""
    base_url = "https://e36a-152-203-184-176.ngrok-free.app"
    url = f"{base_url.rstrip('/')}/{path.lstrip('/')}" if path else base_url

    headers = {
        "ngrok-skip-browser-warning": "true",
        "User-Agent": "ClaudeMCP/1.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        return f"Status: {response.status_code}\nRespuesta:\n{response.text[:3000]}"
    except requests.exceptions.RequestException as e:
        return f"Error en la petición: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
