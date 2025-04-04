# MCTS Tracker MCP Server

A Model Context Protocol (MCP) server that provides real-time Milwaukee County Transit System (MCTS) bus information.

## Overview

This MCP server integrates with the Milwaukee County Transit System (MCTS) API to provide real-time bus arrival predictions. The server exposes a tool that allows AI assistants to retrieve bus arrival times for specific stops in Milwaukee, enhancing the ability of AI models to provide transit information to users.

## Installation


## Configuration

Create a `.env` file in the project root with your MCTS API key:

```
MCTS_API_KEY=your_api_key_here
```

You can obtain an API key from the [Milwaukee County Transit System developer portal](https://www.ridemcts.com/developers).

## Usage

### Running the Server

To start the MCP server:

```bash
python mcts-tracker.py
```

By default, the server uses stdio transport. You can also specify other transport methods as documented in the [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk).

### Available Tools

#### Transit Tools
**get_bus_predictions**: Get real-time arrival predictions for a specific bus stop  


#### get_bus_predictions

Returns real-time bus arrival predictions for a specific stop ID.

**Parameters:**
- `stop_id` (string, required): The ID of the bus stop in Milwaukee.
- `query` (string, optional): Additional query context from the user.

**Example Response:**
```
Stop Name: WISCONSIN + WATER
Stop ID: 4599
Vehicle ID: 5902
Route: 30 (30X)
Direction: EAST
Destination: WISCONSIN & JACKSON
Predicted Arrival Time: 20230515 13:45
Countdown: 5 minutes
Delay: No
Distance to Stop: 5280 feet
Timestamp: 20230515 13:40
Trip ID: 1234
Block ID: 30-1
Type: A
Dynamic: Yes
```

## Integration with AI Assistants

This MCP server is designed to be used with AI assistants that support the Model Context Protocol. When integrated, the AI can use the `get_bus_predictions` tool to retrieve real-time bus information for users.

### Example Query Flow

1. User asks: "When is the next bus arriving at stop 4599?"
2. AI assistant uses the `get_bus_predictions` tool with the stop ID "4599"
3. The MCP server returns formatted arrival predictions
4. AI presents this information to the user in a helpful way

## Development

### Project Structure

```
mcts-mcp/
├── mcts-tracker.py        # Main MCP server entry point
├── pyproject.toml         # Project dependencies and metadata
├── .env                   # API key configuration (not committed to repository)
└── src/
    ├── api/               # API client for MCTS interactions
    │   ├── __init__.py
    │   └── mcts_client.py # MCTS API client implementation
    └── tools/             # MCP tool implementations
        ├── __init__.py
        └── predictions.py # Bus predictions implementation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Model Context Protocol](https://github.com/modelcontextprotocol/mcp) for the framework
- [Milwaukee County Transit System](https://www.ridemcts.com/) for the public transit API