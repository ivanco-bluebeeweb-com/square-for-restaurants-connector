"""Panel UI for Square for Restaurants Connector following UI_INTERFACE_STANDARD.md."""
from __future__ import annotations
from imperal_sdk import ui
from app import ext

def _settings_button() -> ui.UINode:
    return ui.Button(
        "App settings",
        variant="secondary",
        size="sm",
        icon="settings",
        on_click=ui.Call("__panel__square_restaurants_settings")
    )

def _help_modal() -> ui.UINode:
    return ui.Modal(
        trigger=ui.Button("How do I set this up?", variant="ghost", size="sm"),
        title="Connecting Square for Restaurants",
        children=[
            ui.Text(
                "1. Sign in to your Square for Restaurants dashboard and navigate to API/Integration settings.\n"
                "2. Generate an API Key, Token or OAuth credential.\n"
                "3. Enter the details in the form below and click Connect.",
                variant="body"
            )
        ]
    )

@ext.panel("square_restaurants_sidebar", slot="left")
async def main_panel(ctx) -> ui.UINode:
    form = ui.Form(
        submit_label="Connect Square for Restaurants",
        action=ui.Call("connect_square_restaurants"),
        children=[
            ui.Stack(
                direction="v",
                gap=2,
                children=[
                    ui.Stack(
                        direction="v",
                        gap=1,
                        children=[
                            ui.Text("Connection Label", variant="label"),
                            ui.Input(param_name="label", placeholder="e.g. Production Account"),
                        ]
                    ),
                    ui.Stack(
                        direction="v",
                        gap=1,
                        children=[
                            ui.Text("API Key / Access Token", variant="label"),
                            ui.Input(param_name="api_key", placeholder="Paste API Key or Token"),
                        ]
                    ),
                    ui.Stack(
                        direction="v",
                        gap=1,
                        children=[
                            ui.Text("Custom Base URL (optional)", variant="label"),
                            ui.Input(param_name="base_url", placeholder="Leave empty for default"),
                        ]
                    )
                ]
            )
        ]
    )

    return ui.Stack(
        direction="v",
        gap=2,
        children=[
            ui.Heading("Square for Restaurants Connector", level=3),
            ui.Text("Connect and manage your Square for Restaurants workspace.", variant="caption"),
            ui.Divider(),
            form,
            ui.Divider(),
            _help_modal(),
            ui.Divider(),
            _settings_button()
        ]
    )
