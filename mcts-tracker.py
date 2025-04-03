from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("mcts-tracker", "MCTS Tracker Tool")

# Constants for MCTS API
MCTS_API_BASE = "https://realtime.ridemcts.com/bustime/api/v3"
API_KEY = ""  # Replace with your key if needed
USER_AGENT = "mcts-mcp/1.0"


async def make_mcts_request(endpoint: str, params: dict[str, Any]) -> dict[str, Any] | None:
    """Make a request to the MCTS API with error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{MCTS_API_BASE}/{endpoint}", headers=headers, params=params, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error making request to {endpoint}: {e}")
            return None

def format_prediction(prediction: dict) -> str:
    """Format a bus prediction into a readable string."""
    return f"""
Stop Name: {prediction.get('stpnm', 'Unknown')}
Stop ID: {prediction.get('stpid', 'Unknown')}
Vehicle ID: {prediction.get('vid', 'Unknown')}
Route: {prediction.get('rt', 'Unknown')}
Direction: {prediction.get('rtdir', 'Unknown')}
Destination: {prediction.get('des', 'Unknown')}
Predicted Arrival Time: {prediction.get('prdtm', 'Unknown')}
Countdown: {prediction.get('prdctdn', 'Unknown')} minutes
Delay: {'Yes' if prediction.get('dly') else 'No'}
"""


@mcp.tool()
async def get_predictions(stop_id: str) -> str:
    """Get arrival predictions for a specific stop.

    Args:
        stop_id: The ID of the bus stop.
    """
    params = {
        "key": API_KEY,
        "format": "json",
        "stpid": stop_id,
    }
    data = await make_mcts_request("getpredictions", params)

    if not data or "bustime-response" not in data or "prd" not in data["bustime-response"]:
        return "Unable to fetch predictions or no predictions available."

    predictions = [format_prediction(pred) for pred in data["bustime-response"]["prd"]]
    return "\n---\n".join(predictions)


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
