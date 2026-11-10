# genmedia run log, Dusk Delivery art

Date: 2026-11-10 14:51 EST · genmedia 0.7.1

## sheet

```
genmedia run fal-ai/nano-banana-2 --prompt "<sheet prompt>" --aspect_ratio 1:1 --resolution 2K --num_images 1 --download "sheet.{ext}" --json
```

Wall time: 17.4s · price: $0.08/image (listed by `genmedia pricing fal-ai/nano-banana-2`; 2K output may bill higher, check fal billing)

Prompt: Game art for a VERTICAL top-down 3/4 view endless runner. Original character: a tiny courier kid with a red cap and red jacket and an oversized cardboard parcel strapped to their back, running up a city street at dusk. 16-bit pixel art, limited palette (about 24 colors), crisp pixel grid, no anti-aliasing, no blur, warm dusk light. ASSET SHEET on a perfectly flat solid magenta #FF00FF background, six items in two rows of three, evenly spaced and not touching, all in the same top-down 3/4 view and same scale. Top row: (a) the courier seen from behind running away from the camera, left foot forward; (b) the same pose, right foot forward; (c) a stack of cardboard boxes. Bottom row: (d) a striped road barrier with a traffic cone; (e) a glowing envelope with small sparkles; (f) a small puddle. No drop shadows on the background, no text, no labels.

## ground

```
genmedia run fal-ai/nano-banana-2 --prompt "<ground prompt>" --aspect_ratio 9:16 --resolution 2K --num_images 1 --download "ground.{ext}" --json
```

Wall time: 18.8s · price: $0.08/image (listed by `genmedia pricing fal-ai/nano-banana-2`; 2K output may bill higher, check fal billing)

Prompt: Game art for a VERTICAL top-down endless runner, 16-bit pixel art, limited palette, crisp pixel grid, no anti-aliasing, warm dusk light. GROUND TILE: a city street seen from directly above, four lanes separated by three columns of dashed yellow lane markings, the road in the middle 60 percent of the width, light stone sidewalks on both sides, brick building rooftops and windows at the left and right edges, small details like manholes, fallen leaves and cracks. Top and bottom edges seamlessly tileable vertically. No characters, no cars, no obstacles, no text.

## After generation

- Model chosen with `genmedia models "nano banana edit"` and `genmedia pricing`. GPT Image 2.5 Flare was skipped because its listed price is "1 unit" with no per-image figure.
- Both runs are text-to-image from the prompts above, with no reference image.
- The sheet came back with (a)–(f) labels under each item; `tools/extract.py` keeps the six largest shapes, so the labels drop out. The purple drop shadows are removed by the magenta key.
- The ground tile had a row of curb stones at the bottom that breaks vertical tiling; it was trimmed to 1536×2600 (`ground-original.png` is the untouched download).
- The new tile's lanes sit at 0.262 / 0.421 / 0.579 / 0.737 of the width, so the pixel style sets its own `lanes` in `index.html`.
## footage-genmedia / sheet

```
genmedia run fal-ai/nano-banana-2/edit --prompt "<prompt>" --image_urls "[<pixel sheet from the run above>]" --aspect_ratio 1:1 --resolution 2K --num_images 1 --download "sheet.{ext}" --json
```

Wall time: 25.1s · price: $0.08/image listed

Prompt: Restyle this game asset sheet. Keep exactly the same six items in exactly the same positions and sizes, on the same perfectly flat solid magenta #FF00FF background. Remove the (a)-(f) letters: no text or labels anywhere. No shadows on the background. Style: photographic found footage, as if real objects were filmed from above on an old camcorder at dusk: real materials, high ISO noise, crushed blacks, slight chromatic aberration, warm dusk light. The courier is a real kid in a red cap and red jacket with a real cardboard parcel on their back; real cardboard boxes; a real striped road barrier and plastic cone; a real paper envelope with a soft glow; a real rain puddle. Objects cleanly cut out on the magenta background.

## footage-genmedia / ground

```
genmedia run fal-ai/nano-banana-2/edit --prompt "<prompt>" --image_urls "[<pixel ground from the run above>]" --aspect_ratio 9:16 --resolution 2K --num_images 1 --download "ground.{ext}" --json
```

Wall time: 27.1s · price: $0.08/image listed

Prompt: Restyle this top-down street ground tile for a vertical runner game. Keep exactly the same composition: the road in the same place, the three columns of dashed yellow lane markings at exactly the same x positions, sidewalks and building rooftops at the same left and right edges. Top and bottom edges seamlessly tileable vertically. No people, no cars, no obstacles, no text. Style: photographic found footage, as if real objects were filmed from above on an old camcorder at dusk: real materials, high ISO noise, crushed blacks, slight chromatic aberration, warm dusk light.

## gouache-genmedia / sheet

```
genmedia run fal-ai/nano-banana-2/edit --prompt "<prompt>" --image_urls "[<pixel sheet from the run above>]" --aspect_ratio 1:1 --resolution 2K --num_images 1 --download "sheet.{ext}" --json
```

Wall time: 21.8s · price: $0.08/image listed

Prompt: Restyle this game asset sheet. Keep exactly the same six items in exactly the same positions and sizes, on the same perfectly flat solid magenta #FF00FF background. Remove the (a)-(f) letters: no text or labels anywhere. No shadows on the background. Style: hand-painted gouache storybook illustration, visible brush texture, soft muted palette with warm lamplight, flat matte shapes like a picture book. Keep the courier recognisable: red cap, red jacket, oversized cardboard parcel. Objects cleanly cut out on the magenta background.

## gouache-genmedia / ground

```
genmedia run fal-ai/nano-banana-2/edit --prompt "<prompt>" --image_urls "[<pixel ground from the run above>]" --aspect_ratio 9:16 --resolution 2K --num_images 1 --download "ground.{ext}" --json
```

Wall time: 20.2s · price: $0.08/image listed

Prompt: Restyle this top-down street ground tile for a vertical runner game. Keep exactly the same composition: the road in the same place, the three columns of dashed yellow lane markings at exactly the same x positions, sidewalks and building rooftops at the same left and right edges. Top and bottom edges seamlessly tileable vertically. No people, no cars, no obstacles, no text. Style: hand-painted gouache storybook illustration, visible brush texture, soft muted palette with warm lamplight, flat matte shapes like a picture book.

## Found footage and gouache

- The pixel sheet and ground above were uploaded with `genmedia upload` and passed as `image_urls` to `fal-ai/nano-banana-2/edit`, one call per sheet and per ground.
- The gouache sheet kept one stray "(d)" label; `tools/extract.py` drops it with the others.
- Both new ground tiles put the lanes at 0.263 / 0.428 / 0.593 / 0.758 of the width, set as `lanes` for those two styles in `index.html`.
