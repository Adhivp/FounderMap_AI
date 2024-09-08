import plotly.graph_objects as go

def apply_customization_options(fig, layout_option, color_scheme):
    """
    Applies customization options to the Plotly figure.
    """
    
    if layout_option == 'default':
        fig.update_layout(title='Mind Map')
    elif layout_option == 'circular':
        fig.update_layout(
            title='Circular Layout',
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=False, zeroline=False),
        )
    elif layout_option == 'hierarchical':
        fig.update_layout(
            title='Hierarchical Layout',
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=False, zeroline=False),
        )
    else:
        fig.update_layout(title='')

    
    if color_scheme == 'default':
        fig.update_traces(marker=dict(color='blue'))
    elif color_scheme == 'red':
        fig.update_traces(marker=dict(color='red'))
    elif color_scheme == 'green':
        fig.update_traces(marker=dict(color='green'))
    else:
        fig.update_traces(marker=dict(color='blue'))  

    return fig


def create_mind_map(data, layout_option='default', color_scheme='default'):
    """
    Creates a mind map using Plotly from the given data.
    Only shows the legend for one edge and one node.
    """
    try:
        nodes = data['nodes']
        edges = data['edges']

        if not isinstance(nodes, list) or not isinstance(edges, list):
            raise ValueError("Invalid data format: 'nodes' and 'edges' should be lists.")

        node_positions = {node['id']: (node['x'], node['y']) for node in nodes}
        
        edge_traces = []
        for i, edge in enumerate(edges):
            source_id = edge['source']
            target_id = edge['target']

            if source_id not in node_positions or target_id not in node_positions:
                print(f"Warning: Edge with source {source_id} or target {target_id} not found in nodes.")
                continue
            
            x_coords, y_coords = zip(node_positions[source_id], node_positions[target_id])
            
            edge_traces.append(go.Scatter(
                x=x_coords, 
                y=y_coords, 
                mode='lines', 
                line=dict(width=1, color='gray'),
                showlegend=(i == 0),  # Only show legend for the first edge
                name='Edge' if i == 0 else ''
            ))

        node_trace = go.Scatter(
            x=[node['x'] for node in nodes],
            y=[node['y'] for node in nodes],
            mode='markers+text',
            text=[node['label'] for node in nodes],
            marker=dict(size=10, color='blue'),
            showlegend=True,  # Show legend for the first node
            name='Node'  # Legend name for the node
        )

        fig = go.Figure(data=edge_traces + [node_trace])

        fig = apply_customization_options(fig, layout_option, color_scheme)

        return fig

    except Exception as e:
        print(f"Error in create_mind_map: {str(e)}")
        return go.Figure()
