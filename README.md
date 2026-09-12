# CORE Interactive Computer + AI Explorer v7

Fixed interactive Computer Lab simulation.

## What was fixed
- The previous v6 script accidentally replaced the simulation HUD elements while creating the canvas. That caused the simulation JavaScript to crash when it tried to update the missing status elements.
- Removed leftover Three.js CDN dependencies entirely.
- Canvas is now created without deleting the HUD, tooltip, or simulation controls.
- Fixed click detection so selecting a component works reliably after dragging.
- Keeps the dependency-free 2D interactive computer simulation.

## Run
Open `index.html` directly in Chrome/Edge, or serve the folder with any static server.
No Node.js, npm, CDN, or internet connection is required.
