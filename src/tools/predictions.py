from typing import Any, Dict
from src.api.mcts_client import get_predictions_data

def format_prediction(prediction: dict) -> str:
    """Format a bus prediction into a readable string."""
    return f"""
Stop Name: {prediction.get('stpnm', 'Unknown')}
Stop ID: {prediction.get('stpid', 'Unknown')}
Vehicle ID: {prediction.get('vid', 'Unknown')}
Route: {prediction.get('rt', 'Unknown')} ({prediction.get('rtdd', '')})
Direction: {prediction.get('rtdir', 'Unknown')}
Destination: {prediction.get('des', 'Unknown')}
Predicted Arrival Time: {prediction.get('prdtm', 'Unknown')}
Countdown: {prediction.get('prdctdn', 'Unknown')} minutes
Delay: {'Yes' if prediction.get('dly') else 'No'}
Distance to Stop: {prediction.get('dstp', 'Unknown')} feet
Timestamp: {prediction.get('tmstmp', 'Unknown')}
Trip ID: {prediction.get('tatripid', 'Unknown')}
Block ID: {prediction.get('tablockid', 'Unknown')}
Type: {prediction.get('typ', 'Unknown')}
Dynamic: {'Yes' if prediction.get('dyn') else 'No'}
"""


async def get_predictions(stop_id: str, query: str = "") -> str:
    """Get arrival predictions for a specific stop in Milwaukee.

    Args:
        stop_id: The ID of the bus stop in Milwaukee.
        query: The user's query that will be checked for Milwaukee-related content.
    """
    # if  is_milwaukee_related(query):
    #     return "This tool only processes queries related to Milwaukee public transportation."

    data = await get_predictions_data(stop_id)

    if not data or "bustime-response" not in data or "prd" not in data["bustime-response"]:
        return "Unable to fetch predictions or no predictions available."

    predictions = [format_prediction(pred) for pred in data["bustime-response"]["prd"]]
    return "\n---\n".join(predictions)