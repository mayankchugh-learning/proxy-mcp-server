import os
from pathlib import Path

from dotenv import load_dotenv
from fastmcp import FastMCP

# Claude Desktop often starts MCP with cwd System32; load `.env` next to this file.
load_dotenv(Path(__file__).resolve().parent / ".env")

# FastMCP Cloud requires auth. Set FASTMCP_REMOTE_TOKEN in `.env` or the environment
# deployment dashboard (same token you would put after "Bearer " in Authorization).
# Do not commit real tokens; use env or your MCP client config only.
REMOTE_URL = "https://rapid-crimson-roundworm.fastmcp.app/mcp"
_token = os.environ.get("FASTMCP_REMOTE_TOKEN", "").strip()
if not _token:
    raise RuntimeError(
        "Missing FASTMCP_REMOTE_TOKEN. In the FastMCP Cloud / Horizon UI, open your server, "
        "copy the API / Bearer token for this deployment, then set the env var (no 'Bearer ' prefix)."
    )

mcp = FastMCP.as_proxy(
    {
        "mcpServers": {
            "remote": {
                "url": REMOTE_URL,
                "transport": "http",
                "auth": _token,
            }
        }
    },
    name="Mayank Server Proxy",
)

if __name__ == "__main__":
    # This runs via STDIO, which Claude Desktop can connect to
    mcp.run()