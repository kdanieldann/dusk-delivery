# Dusk Delivery

A tiny vertical runner for the browser. You're a courier with a parcel too big for your back, running up a city street at dusk. Switch lanes, dodge boxes, barriers and puddles, and pick up the envelopes.

**Play:** [kdanieldann.github.io/dusk-delivery](https://kdanieldann.github.io/dusk-delivery/)

## Controls

- **← →** or **A / D** to switch lanes (swipe or tap on mobile)
- **0–3** to switch art style

## One game, four looks

The game started as plain coloured blocks. The same layout was then drawn in three styles, and every style can be swapped in while you play:

| Key | Style |
|---|---|
| 0 | blocks (the original programmer art) |
| 1 | 16-bit pixel art |
| 2 | found footage |
| 3 | gouache storybook |

Each style is a folder in `assets/` with the same file names, so adding a fifth look means adding one folder and one line in `STYLES`.

## URL options

- `?style=pixel` start in a given style
- `?auto` autopilot: the courier plays itself (handy for recording)
- `?clean` hide the score and style buttons

## How it was made

- Game code: written with Claude Code, one HTML file, no build step.
- Art: generated with [genmedia](https://genmedia.sh) on fal, six Nano Banana 2 calls. The pixel set came first from text prompts; found footage and gouache restyle it with the edit endpoint, so items and lanes line up. Commands, prompts and timings are in [`genmedia-log.md`](genmedia-log.md).
- `tools/extract.py` cuts sprites out of each generated sheet (magenta key), shrinks them to web sizes and exports the ground tile. Styles whose ground tile has a different lane layout set their own `lanes` in `STYLES`.

## Run locally

```
python3 -m http.server
```

then open http://localhost:8000.
