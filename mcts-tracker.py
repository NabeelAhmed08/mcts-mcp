from typing import Any, List, Dict, Union
import os
from mcp.server.fastmcp import FastMCP
from src.tools.predictions import get_predictions

# Initialize FastMCP server
mcp = FastMCP("mcts-tracker", "MCTS Tracker Tool")

@mcp.tool()
async def get_bus_predictions(stop_id: str, query: str = "") -> str:
    """Get arrival predictions for a specific stop in Milwaukee.

    Args:
        stop_id: The ID of the bus stop in Milwaukee.
        query: The user's query that will be checked for Milwaukee-related content.
    """
    return await get_predictions(stop_id, query)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
