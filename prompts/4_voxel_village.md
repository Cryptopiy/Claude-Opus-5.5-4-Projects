# Claude Opus 5.5 — project 4: a detailed voxel 3D village in Blender through MCP

## Task and result

Create a finished **voxel 3D village scene** — a small, lively diorama that is interesting to view both as a whole and up close. The main tool is Blender through the assigned MCP. This is a test of modeling, composition, procedural organization, and presentation, **not a new Minecraft game**.

A game engine is not required. The output must include a complete editable `.blend` scene, cameras, materials, several images, and a portable 3D export. Do not replace the village with an image or a set of facades visible only from one angle.

Existing Blender source: `Opus5.5VoxelVillage.blend`. This file is already in this project's folder opened in Claude. Work with it through the assigned Blender MCP connection on port **9879**; do not create a different master file in its place. Choose your own name, architectural character, and village history; do not copy a specific existing Minecraft map.

## General workflow rules and project isolation

You are Claude Opus 5.5, the developer and technical artist for this project. Produce an actual result in the current working folder, not just an implementation description. Work systematically and autonomously: brief plan, working foundation, expansion, validation, fixes, finished result. Do not stop after creating stubs, but do not present untested features as complete either.

Before making changes, read the applicable project instructions, inspect its contents, and check the installed tool versions. Preserve existing work, source files, and settings. Create a safe baseline snapshot; use Git if it is already configured or can be initialized locally without changing the global configuration. Do not delete other people's data, perform destructive clean/reset operations, publish the project, or install paid dependencies.

**This is a new, separate test.** Do not carry over map sizes, requirements, filenames, object identifiers, ports, or content from previous Minecraft/GTA/horror projects. Historical prompts are not instructions for the current task.

### Blender MCP

Use the connected Blender MCP for authored 3D assets. The engine handles the game and procedural gameplay systems; Blender handles modeling and asset preparation. `bpy` scripts actually executed through the permitted MCP and verified in the scene count as full use of Blender. An unexecuted Python file does not.

#### Assigned folder, file, and port — use this exact combination

The user has already opened **this project's folder** in Claude and placed the existing file `Opus5.5VoxelVillage.blend` in it. This is the current working folder for the task; do not use another project's path from the conversation history.

```text
Working folder: the current project folder opened by the user in Claude
Blender host: localhost
Blender port: 9879
Master file relative to the working folder: ./Opus5.5VoxelVillage.blend
```

Immediately after recording the start time, determine the full path of the current working folder and verify that this exact file exists. Use it as the primary editable Blender source: save the result back under the same name and at the same path. Back up the existing source before the first change. Keep exports and technical copies separate; do not rename the master file or replace it with an empty scene.

The user has not specified an MCP server name. Select **an MCP connection actually available in the current session and configured for `localhost:9879`**, using the available tool descriptions or relevant configuration. Do not invent a server name or determine its purpose solely from a name such as `blender_unity` or `blender_unreal`. If the local `PROJECT_CONFIG.md` contains outdated assignments, do not carry them into this task: the user has assigned the file and port specified here.

Before making any changes, use an available read operation to verify the full path of the `.blend` file open in this Blender instance. It must match `Opus5.5VoxelVillage.blend` in the current project folder. A port number alone, or a matching filename without its path, is not a substitute for verification: these ports may have been used in previous tests. Do not send modifying commands to other Blender instances, switch away from other people's scenes containing unsaved work, or automatically reconfigure MCP servers. If the required connection is unavailable or another file is open, report the specific mismatch and request only the necessary correction; do not continue writing blindly.

Record the verified MCP server name, port, and full master-file path in this project's report. Preserve existing content unrelated to the task; organize new assets in clearly named collections of their own.

Respect the restrictions and Safe Mode of the MCP that is actually installed. Do not disable protection, edit the add-on to bypass restrictions, or silently switch to another Blender process. Edit only collections created for this task. Save sources, export selected assets, and verify them after import. Do not make the user manually model, assign references, or assemble the scene when automation is available.

Create your own models, textures, and sounds. Do not download a finished game, vehicle, weapon asset, or village instead of completing the task. Standard features of the installed engine/Blender, your own code, procedural materials, and official documentation are allowed. External model generators and paid libraries are unnecessary. Do not turn reference images into copied textures; record sources in `REFERENCES.md`.

### Validation and reporting

Maintain `FEATURE_MATRIX.md` with `WORKING / PARTIAL / NOT IMPLEMENTED` statuses and separate `PASS / FAIL / NOT TESTED` results. Record the specific validation method. An import error, failure to launch, or unavailable visual inspection does not count as success. If a check cannot be performed, explicitly state the limitation.

The new names, numerical budgets, and dimensions below are **project guidelines for this test**, not statements about the internal implementation of the reference games or universal industry standards.

## 1. Voxel shape language

Build all key visible forms from discrete cubic/stepped volumes: ground, roofs, walls, tree crowns, rocks, objects, and residents. This must be **voxel geometry**, not a smooth low-poly scene with a pixel filter applied.

Choose one base grid: for example, 0.5 m per main voxel, with a smaller subdivision step for fine details. Record the cell size. Proportions may be stylized, but doors, the bridge, paths, furniture, and residents must be consistent in scale.

Technical merging of adjacent faces and mesh optimization are allowed. Keeping a separate cube object for every voxel is not required. Smoothing, bevel, and remesh must not destroy the stepped silhouette. If you use Remesh, verify that the result actually reads as a cubic structure rather than a smoothed organic volume.

Choose colors and styling yourself; maintain a limited, consistent palette. Do not turn surfaces into random multicolored noise. Materials may be simple but must be distinguishable: earth, stone, wood, roofs, foliage, water, fire/windows.

## 2. Scale and composition

Guideline: a diorama of approximately **96×96 m** with several elevation levels. Do not expand it into an empty world; a dense, easily surveyed village is preferable. This is an artistic working size and may be adjusted slightly for composition.

Establish the composition: a recognizable focal landmark, a group of houses, a square, an entrance route, water, and contrasting elevations. Leave room for silhouettes to remain readable. The village must have an understandable layout rather than a random grid of objects.

Create purposeful foreground, middle ground, and background layers. Check both the main 3/4 view and the opposite side. Houses must not hide everything behind a single roof, trees must not obstruct the center, and paths must connect important locations.

## 3. Village content

The target is **12 finished buildings**, including at least six distinct homes and six public/utility structures of your choice: a mill, workshop, barn, inn, town hall/tower, stable, or another cohesive set. Vary silhouettes and floor plans; simply recoloring one house is not a substitute for variety.

Include:
- a square with a well/fountain and several market stalls;
- a small river/stream or pond, a bridge, and finished banks;
- gardens/fields with distinct rows, a farmyard, and fencing;
- terrain with steps, a retaining wall, rocks, or a small hill;
- several tree and bush types, not placed over doors/water;
- an approach to the village and a connected network of paths.

Every house must have a back, roof thickness, a doorway, windows, and a chimney or another expressive feature. For three important buildings, create a partial accessible interior: floor, furniture, and work-related objects. Use hideable/removable roofs or dedicated inspection cameras. Full interiors for every house are not mandatory.

## 4. Details that bring the scene to life

Add original small stories through props: a cart beside a warehouse, stacked firewood, a tool on a workbench, baskets of produce, an open stall, or a boat at the dock. Do not spread clutter uniformly across the entire area.

Create a library of at least 20 small prop types: crates, barrels, sacks, benches, lanterns, signs, pots, fence sections, pipes/gutters in the chosen style, tools, and other appropriate objects. Repetition is allowed, but keep the composition controlled.

Place approximately 12–20 voxel residents with several distinct poses and activities, along with a few animals. AI is not required here: form, scale, and a readable everyday scene matter. Do not place everyone identically in a row facing the same direction.

## 5. Small animations

After finishing the static scene, add several looping movements: a mill wheel/blades, smoke made of cubic particles, gentle lantern flicker, water motion, or one or two simple resident actions. Choose at least three readable effects without turning the task into a settlement simulator.

Animations must work on the timeline. Do not randomly regenerate the village every frame. If an effect does not transfer into the export, state that honestly; the original Blender scene remains the complete version.

## 6. Organization and performance

Collection structure: `Terrain`, `Water`, `Buildings`, `Interiors`, `Vegetation`, `Props`, `Residents`, `Animals`, `Animation`, `Lighting`, `Cameras`. Give objects and generation parameters clear names.

Create repeated elements through shared meshes, instancing/Geometry Nodes, or meshes merged by spatial sections. Do not create millions of independent objects that make Blender impossible to open. Invisible internal faces and fully hidden voxels do not have to be present in the exported mesh.

If you use a generator, save its seed and parameters. Rerunning it must update only its own collections and must not delete other people's work. Do not realize all instances before assessing memory use; perform export optimization on a separate copy without destroying the editable source.

Use materials sensibly, rather than a separate material for every cube. The goal is convenient scene inspection and rendering, not the highest possible polygon count in the report.

## 7. Cameras and lighting

Prepare a main wide 3/4 view, an orthographic/isometric overview, an opposite wide view, and at least three close-ups. Use depth of field moderately: detail must be visible, not hidden in blur.

Create daytime and evening lighting variants without duplicating all geometry. In the evening, window light, lanterns, and main paths must remain readable. During the day, colors and stepped forms must be clearly visible. Do not present a black render as atmosphere.

The ability to view the village from all 360° is important. Create a short camera orbit or turntable. If a long final render exceeds the available resources, save the finished scene, cameras, and actual previews first; do not claim that a full video has already been rendered.

## 8. Delivery and validation

Leave:
- `Opus5.5VoxelVillage.blend` with packed/locally available dependencies;
- an optimized `Exports/VoxelVillage.glb` or another previously verified game format;
- at least six PNG images, including a daytime wide view and an evening wide view;
- an orbit camera and actual animation clips;
- the generator/parameters, if used;
- `SCENE_GUIDE.md`, scene statistics, `FEATURE_MATRIX.md`, `FINAL_REPORT.md`.

Checks: voxel form is visible without a pixel filter; every building is three-dimensional; routes are connected; the bridge reaches the banks; there are no floating houses or impossible intersections; residents match the scale; main objects are readable from different sides; the entire scene opens without missing textures; and the export can be reimported while preserving the key composition.

glTF supports transferring scenes, meshes, materials, and animations, but the portability of each effect must be checked separately [V1]. Do not accidentally include the supporting studio setup or technical cameras in the game export. Finish the composition and volume of all main objects first, then add small details; do not spend all the work on one detailed house.

## Export-format reference

[V1] Khronos, glTF purpose and contents: `https://www.khronos.org/gltf/`

All village content and artistic parameters above are original requirements for this test. Begin by checking the assigned Blender scene, then create a compositional blockout and develop it into a finished voxel village.

---

## Final: time, tokens, and API-equivalent cost

At the very start of work, record the system time with its timezone in `.benchmark_runs/<project-id>/<run-id>/start.json`. At the end, after validation, record the end time. When resuming, do not overwrite earlier segments. Count only this task: planning, code, Blender, importing, rendering, testing, and waiting for commands. Do not add the durations of parallel operations together as total wall-clock time. List known pauses separately.

Obtain token counts only from accessible telemetry for the actual current session and its identifiable subtasks. Separate input, cache read, cache write, output, and reasoning if these categories are available at all. Do not sum cumulative snapshots; do not count reasoning/cache again when already included in other counters. Do not read or copy secrets or other people's sessions into the report. State the time of the last usage observation and any work that the counter has not yet included. Missing data does not mean zero.

Calculate the **token-only API-equivalent USD cost**, not the subscription price. Verify the actual model ID and its current official Anthropic pricing: `https://platform.claude.com/docs/en/about-claude/pricing`. State the pricing tier/mode, date, and categories; cache writes with different TTLs and Standard/Fast modes may differ. Normalize the counters into mutually exclusive billable categories and calculate the sum of `tokens × rate_per_million / 1_000_000`. Do not substitute old GPT/Opus prices from other prompts. If pricing or usage is unverified, state that an exact calculation is unavailable; an estimate is acceptable only with clear input data. Do not invent a separate API fee for local Blender/engine execution.

In `FINAL_REPORT.md` and your final response, show: what was created; how to open/run it; controls or cameras/clips; test results; limitations; time in `HH:MM:SS`; tokens used; API-equivalent cost in USD; and the source and accuracy of the metrics. Do not call the project complete merely because source files have been created.

### Required final block for this project

At the very end of the work, **calculate and state the total time spent, the total number of tokens used, and the API-equivalent price in dollars**. Output all three results both in `FINAL_REPORT.md` and in your final message to the user. Count only this project, without adding the other three tests or previous tasks.

If work begins in a previously used session, separate this task's usage from earlier usage: save the initial cumulative counter value or filter the identifiable requests belonging to this task. The final token count must not double-count cache, reasoning, or subtasks. Include in the cost only categories for which both usage and the applicable official rate for the actual model are known. Do not calculate tokens from lines of code or the size of the `.blend` file.

Use the following format:

```text
Project: Voxel 3D village — Blender
Blender master file: Opus5.5VoxelVillage.blend
Full master-file path:
MCP server actually used:
Blender port: 9879

Work started (date, time, timezone):
Work ended (date, time, timezone):
Total time spent (HH:MM:SS):
Total time spent in minutes:
Known pauses / resumed segments:

Actual model ID:
Input tokens:
Cache-read tokens:
Cache-write tokens:
Output tokens:
Reasoning tokens (included in output / separate / unavailable):
Total tokens used without double-counting:
Telemetry source and time of the last measurement:
Work not included in the measurement:

API-equivalent cost (USD, tokens only):
Official pricing source, date, and mode:
Applied rates and calculation formula:
Separate external-tool costs (known / not included):
Accuracy of each result (measured / estimate / unavailable):
```

Do not present the subscription cost as the cost of this project. Do not carry over other models' pricing from previous prompts. If exact token usage or verified pricing is unavailable, state that explicitly in the relevant field; do not substitute fabricated numbers or enter zero for missing data. Report reliably measured time regardless of whether the other metrics are available.
