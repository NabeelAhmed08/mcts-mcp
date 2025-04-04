from typing import Any, Dict, Optional
import httpx
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants for MCTS API
MCTS_API_BASE = "https://realtime.ridemcts.com/bustime/api/v3"
API_KEY = os.getenv("MCTS_API_KEY")  # Load API key from environment variables
USER_AGENT = "mcts-mcp/1.0"


async def make_mcts_request(endpoint: str, params: dict[str, Any]) -> dict[str, Any] | None:
    """Make a request to the MCTS API with error handling.
    
    Args:
        endpoint: The API endpoint to call (e.g., "getpredictions")
        params: The query parameters to include in the request
        
    Returns:
        The JSON response as a dictionary, or None if the request failed
    """
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
    }
    
    # Add required API parameters
    params["key"] = API_KEY
    params["format"] = "json"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{MCTS_API_BASE}/{endpoint}", 
                headers=headers, 
                params=params, 
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as e:
            print(f"Network error requesting {endpoint}: {e}")
            return None
        except httpx.HTTPStatusError as e:
            print(f"HTTP error requesting {endpoint}: {e.response.status_code}")
            return None
        except Exception as e:
            print(f"Unexpected error making request to {endpoint}: {e}")
            return None


async def get_predictions_data(stop_id: str) -> dict[str, Any] | None:
    """Get raw prediction data for a specific stop ID.
    
    Args:
        stop_id: The ID of the MCTS bus stop
        
    Returns:
        Raw API response data or None if the request failed
    """
    params = {
        "stpid": stop_id,
    }
    return await make_mcts_request("getpredictions", params)