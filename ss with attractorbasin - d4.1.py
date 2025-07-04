import numpy as np
import plotly.graph_objs as go

# 1) Create grid of x and y
num_points = 50
x_vals = np.linspace(0, 1, num_points)
y_vals = np.linspace(0, 1, num_points)
X, Y = np.meshgrid(x_vals, y_vals)

# 2) Define z-values
Z = -np.exp(-((X - 0.8)**2 + (Y - 0.8)**2) / 0.02)

surface = go.Surface(
    x=X,
    y=Y,
    z=Z,
    colorscale="rdbu",
    showscale=True,
    contours={
        # 3) Z-contours (topographic lines on the surface)
        "z": {
            "show": True,
            "start": Z.min(),
            "end": 0,
            "size": abs(Z.min() / 8),
            "color": "white",
            "project": {"z": True}
        },
        # 4) X- and Y-contours (wireframe grid lines)
        "x": {
            "show": True, 
            "start": X.min(),
            "end": X.max(),
            "size": (X.max() - X.min()) / 16,  # spacing between lines
            "color": "lightgray",
            "project": {"x": True}
        },
        "y": {
            "show": True, 
            "start": Y.min(),
            "end": Y.max(),
            "size": (Y.max() - Y.min()) / 16,
            "color": "lightgray",
            "project": {"y": True}
        },
    }
)
fig = go.Figure(data=[surface])

# 4) Configure layout
fig.update_layout(
    title="2D State Space with an Attraction Basin & Contour Lines",
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectratio=dict(x=1, y=1, z=0.2)
    )
)

fig.show()
