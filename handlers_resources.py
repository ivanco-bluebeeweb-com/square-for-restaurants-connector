"""Resource handlers for Square for Restaurants Connector."""
from __future__ import annotations
from typing import Any
from imperal_sdk import ActionResult
from app import chat
from schemas import (
    ListOrderParams, GetOrderParams,
    OrderRecord, OrderList, AuditHealthReport, ConnectionIdParams
)
from handlers_connection import resolve_client

@chat.function("list_orders", "List orders in Square for Restaurants.", action_type="read", chain_callable=True, event="square-for-restaurants-connector.list_orders", effects=["read:orders"], data_model=OrderList)
async def list_orders(params: ListOrderParams, ctx) -> ActionResult:
    client = await resolve_client(ctx, params.connection_id)
    try:
        raw_items = await client.list_orders(limit=params.limit)
        items = []
        for r in raw_items:
            rid = str(r.get("id") or r.get("key") or r.get("uuid") or "unknown")
            rname = r.get("name") or r.get("title") or r.get("label") or rid
            items.append({"id": rid, "name": rname, "status": r.get("status"), "created_at": r.get("createdAt") or r.get("created_at"), "raw": r})
        return ActionResult.ok({"orders": items, "total": len(items)}, summary=f"Found {len(items)} orders.")
    except Exception as e:
        return ActionResult.error(f"Error listing orders: {e}")

@chat.function("get_order", "Get details of one Order in Square for Restaurants.", action_type="read", chain_callable=True, event="square-for-restaurants-connector.get_order", effects=["read:order"], data_model=OrderRecord)
async def get_order(params: GetOrderParams, ctx) -> ActionResult:
    client = await resolve_client(ctx, params.connection_id)
    try:
        r = await client.get_order(params.order_id)
        rid = str(r.get("id") or params.order_id)
        rname = r.get("name") or r.get("title") or rid
        return ActionResult.ok({"id": rid, "name": rname, "status": r.get("status"), "created_at": r.get("createdAt") or r.get("created_at"), "raw": r}, summary=f"Retrieved Order {rid}.")
    except Exception as e:
        return ActionResult.error(f"Error retrieving Order: {e}")

@chat.function("audit_order_health", "Audit health of Square for Restaurants orders and connectivity.", action_type="read", chain_callable=True, event="square-for-restaurants-connector.audit_order_health", effects=["read:audit"], data_model=AuditHealthReport)
async def audit_order_health(params: ConnectionIdParams, ctx) -> ActionResult:
    client = await resolve_client(ctx, params.connection_id)
    try:
        items = await client.list_orders(limit=50)
        return ActionResult.ok({
            "healthy": True,
            "total_orders": len(items),
            "details": {"sample_count": len(items)},
            "summary": f"Square for Restaurants healthy. Sampled {len(items)} orders."
        }, summary=f"Square for Restaurants health check passed with {len(items)} orders.")
    except Exception as e:
        return ActionResult.error(f"Error auditing Square for Restaurants health: {e}")
