from .atri import Atri
from fastapi import Request, Response
from atri_utils import *

def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    at.BarChart1.custom.data = [
    {
        "x": "2010",
        "temperature": 20,
        "rainfall": 10
    },
    {
        "x": "2011",
        "temperature": 30,
        "rainfall": 20
    },
    {
        "x": "2012",
        "temperature": 20,
        "rainfall": 15
    }
    ]

    at.LineChart1.custom.data = [
    {
        "x": "2010",
        "temperature": 20,
        "rainfall": 10
    },
    {
        "x": "2011",
        "temperature": 30,
        "rainfall": 20
    },
    {
        "x": "2012",
        "temperature": 20,
        "rainfall": 15
    }
    ]

    at.PieChart1.custom.data = [
    # Inner circle
    [
        { "name": "Group A", "value": 400 },
        { "name": "Group B", "value": 300 },
        { "name": "Group C", "value": 300 },
        { "name": "Group D", "value": 200 },
    ],
    # Outer circle
    [
        { "name": "A1", "value": 100 },
        { "name": "A2", "value": 300 },
        { "name": "B1", "value": 100 },
        { "name": "B2", "value": 80 },
    ]
    ]

    at.AreaChart1.custom.data = [
    {
        "x": "2010",
        "temperature": 20,
        "rainfall": 10
    },
    {
        "x": "2011",
        "temperature": 30,
        "rainfall": 20
    },
    {
        "x": "2012",
        "temperature": 20,
        "rainfall": 15
    }
    ]
    pass

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    at.BarChart1.custom.data = [
    {
        "x": "2010",
        "temperature": 20,
        "rainfall": 10
    },
    {
        "x": "2011",
        "temperature": 30,
        "rainfall": 20
    },
    {
        "x": "2012",
        "temperature": 20,
        "rainfall": 15
    }
    ]

    at.LineChart1.custom.data = [
    {
        "x": "2010",
        "temperature": 20,
        "rainfall": 10
    },
    {
        "x": "2011",
        "temperature": 30,
        "rainfall": 20
    },
    {
        "x": "2012",
        "temperature": 20,
        "rainfall": 15
    }
    ]

    at.PieChart1.custom.data = [
    # Inner circle
    [
        { "name": "Group A", "value": 400 },
        { "name": "Group B", "value": 300 },
        { "name": "Group C", "value": 300 },
        { "name": "Group D", "value": 200 },
    ],
    # Outer circle
    [
        { "name": "A1", "value": 100 },
        { "name": "A2", "value": 300 },
        { "name": "B1", "value": 100 },
        { "name": "B2", "value": 80 },
    ]
    ]

    at.AreaChart1.custom.data = [
    {
        "x": "2010",
        "temperature": 20,
        "rainfall": 10
    },
    {
        "x": "2011",
        "temperature": 30,
        "rainfall": 20
    },
    {
        "x": "2012",
        "temperature": 20,
        "rainfall": 15
    }
    ]
    pass

def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    pass