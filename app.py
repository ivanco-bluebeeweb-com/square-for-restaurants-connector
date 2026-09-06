"""Extension declaration, capabilities, health check for Square for Restaurants Connector."""
from __future__ import annotations
import json
from imperal_sdk import ChatExtension, Extension

ext = Extension(
    "square-for-restaurants-connector",
    version="0.1.0",
    display_name="Square for Restaurants",
    icon="icon.svg",
    capabilities=["square_restaurants:manage"],
    description="Official Imperal connector for Square for Restaurants (C30. Email Marketing & Newsletter). Manage operations securely."
)

chat = ChatExtension(ext)

@ext.health_check
async def health_check(ctx) -> dict:
    raw = await ctx.secrets.get("square_restaurants_connections")
    try:
        count = len(json.loads(raw)) if raw else 0
    except Exception:
        count = 0
    return {
        "healthy": True,
        "detail": f"{count} Square for Restaurants connection(s) configured." if count else "Not connected yet."
    }
