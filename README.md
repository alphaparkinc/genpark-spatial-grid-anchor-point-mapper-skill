# genpark-spatial-grid-anchor-point-mapper-skill

Alphanumeric viewport grid and anchor point mapper translating continuous vision bounding boxes into deterministic click coordinates for computer-use GUI agents.

## Architecture

```mermaid
flowchart LR
    Box[Detected UI Element Box] --> CenterCalc[Center Point Calculator]
    CenterCalc --> GridMapper[Alphanumeric Grid Discretizer]
    GridMapper --> ClickEvent[Click Target (x, y) & Cell A1..H6]
```

## Features
- **Configurable Viewport**: Supports 1080p, 1440p, 4K and custom dimensions.
- **Alphanumeric Cell Coordinates**: Provides human-interpretable reasoning labels (e.g., "B2").
