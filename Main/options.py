def get_startup_options():
    """
    Provides predefined mind map options for startup ideas.
    """
    return {
        "Basic Structure": {
            "description": "A simple hierarchical structure for ideas.",
            "layout": "Tree",
        },
        "Flow Diagram": {
            "description": "Best for sequential steps.",
            "layout": "Flow",
        },
        "Network": {
            "description": "Ideal for complex relationships.",
            "layout": "Network",
        },
    }

def get_customization_options():
    """
    Provides customization options for mind maps.
    """
    return {
        "Layouts": ["Default", "Circular", "Tree", "Radial"],
        "Colors": ["Blue", "Red", "Green", "Monochrome"],
        "Additional Features": ["Grid", "Node Size Variations"],
    }
