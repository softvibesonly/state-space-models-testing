# state-space-models-testing
Trying to build a state space model

This is a tiny sandbox sketch I made while trying to wrap my head around how attractor basins show up in state space models. It’s not a formal simulation—just a 3D surface plot using Plotly to help me visualize what it might feel like for a dynamical system to “fall into” a region of stability.

The surface is generated from a Gaussian bump centered at (0.8, 0.8), negated to simulate a “dip” or “basin” that attracts trajectories. The contour lines on the X, Y, and Z planes are there mostly to help me get my bearings and see what the gradient field might imply about flow. I needed something low-stakes and intuitive to orient myself before diving into more serious modeling (like using actual ODEs or working through the Dirichlet function properly).

**Why this exists:**

Because I was getting frustrated with abstract definitions of attractors and wanted something I could see. I’ve been learning about state spaces, limit cycles, and chaotic systems, and I’m trying to train my visual intuition for what “structure” looks like in a dynamical system—especially as I move toward understanding neural dynamics and memory storage in things like Hopfield networks and Boltzmann machines.

Requirements
	•	Python 3
	•	plotly
	•	numpy

Install via pip if you don’t already have them.
In bash, just type: pip install plotly numpy

**Running the Script**
Just run in bash:
python "ss with attractorbasin - d4.1.py"

This will launch an interactive 3D plot in your browser. You can rotate, zoom, and pan around to inspect the shape of the surface and its contours. I'll try to build on this to work on making more complex models later (who knows how long)
