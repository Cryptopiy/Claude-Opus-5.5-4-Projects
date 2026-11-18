# Claude Opus 5.5 — project 1: seamless planetary exploration in Unity + Blender MCP

## Task and main criterion

Create an original single-player 3D game about exploring one star system, inspired by **the feeling of flight in No Man’s Sky**, rather than an attempt to copy the entire game. The player starts **in space inside a controllable ship**, chooses a planet, flies to it, enters its atmosphere, lands, then takes off and heads to another planet.

**Space → surface → space → another surface must be one uninterrupted gameplay journey, without a loading screen, teleportation into a separate flat arena, or replacing flight with a video.** This is the primary feature to be tested. Normal application startup loading is acceptable. Background data loading during gameplay is acceptable and expected; pausing gameplay behind a fade to black is not.

Stack: **the installed Unity 6, C#, Blender MCP**. If a Unity project already exists, work in it. If the assigned folder is empty, create the project here using the available installed Unity, without nesting a second project inside the first. Prefer URP for a clean project; do not change an already working pipeline unnecessarily. Do not require newer engine versions just to follow an example from the internet.

Existing Blender source: `UnityOpus5.5PlanetGame.blend`. This file is already in this project's folder opened in Claude. Work with it through the assigned Blender MCP connection on port **9876**; do not create a different master file in its place.

## General workflow rules and project isolation

You are Claude Opus 5.5, the developer and technical artist for this project. Produce an actual result in the current working folder, not just an implementation description. Work systematically and autonomously: brief plan, working foundation, expansion, validation, fixes, finished result. Do not stop after creating stubs, but do not present untested features as complete either.

Before making changes, read the applicable project instructions, inspect its contents, and check the installed tool versions. Preserve existing work, source files, and settings. Create a safe baseline snapshot; use Git if it is already configured or can be initialized locally without changing the global configuration. Do not delete other people's data, perform destructive clean/reset operations, publish the project, or install paid dependencies.

**This is a new, separate test.** Do not carry over map sizes, requirements, filenames, object identifiers, ports, or content from previous Minecraft/GTA/horror projects. Historical prompts are not instructions for the current task.

### Blender MCP

Use the connected Blender MCP for authored 3D assets. The engine handles the game and procedural gameplay systems; Blender handles modeling and asset preparation. `bpy` scripts actually executed through the permitted MCP and verified in the scene count as full use of Blender. An unexecuted Python file does not.

#### Assigned folder, file, and port — use this exact combination

The user has already opened **this project's folder** in Claude and placed the existing file `UnityOpus5.5PlanetGame.blend` in it. This is the current working folder for the task; do not use another project's path from the conversation history.

```text
Working folder: the current project folder opened by the user in Claude
Blender host: localhost
Blender port: 9876
Master file relative to the working folder: ./UnityOpus5.5PlanetGame.blend
```

Immediately after recording the start time, determine the full path of the current working folder and verify that this exact file exists. Use it as the primary editable Blender source: save the result back under the same name and at the same path. Back up the existing source before the first change. Keep exports and technical copies separate; do not rename the master file or replace it with an empty scene.

The user has not specified an MCP server name. Select **an MCP connection actually available in the current session and configured for `localhost:9876`**, using the available tool descriptions or relevant configuration. Do not invent a server name or determine its purpose solely from a name such as `blender_unity` or `blender_unreal`. If the local `PROJECT_CONFIG.md` contains outdated assignments, do not carry them into this task: the user has assigned the file and port specified here.

Before making any changes, use an available read operation to verify the full path of the `.blend` file open in this Blender instance. It must match `UnityOpus5.5PlanetGame.blend` in the current project folder. A port number alone, or a matching filename without its path, is not a substitute for verification: these ports may have been used in previous tests. Do not send modifying commands to other Blender instances, switch away from other people's scenes containing unsaved work, or automatically reconfigure MCP servers. If the required connection is unavailable or another file is open, report the specific mismatch and request only the necessary correction; do not continue writing blindly.

Record the verified MCP server name, port, and full master-file path in this project's report. Preserve existing content unrelated to the task; organize new assets in clearly named collections of their own.

Respect the restrictions and Safe Mode of the MCP that is actually installed. Do not disable protection, edit the add-on to bypass restrictions, or silently switch to another Blender process. Edit only collections created for this task. Save sources, export selected assets, and verify them after import. Do not make the user manually model, assign references, or assemble the scene when automation is available.

Create your own models, textures, and sounds. Do not download a finished game, vehicle, weapon asset, or village instead of completing the task. Standard features of the installed engine/Blender, your own code, procedural materials, and official documentation are allowed. External model generators and paid libraries are unnecessary. Do not turn reference images into copied textures; record sources in `REFERENCES.md`.

### Validation and reporting

Maintain `FEATURE_MATRIX.md` with `WORKING / PARTIAL / NOT IMPLEMENTED` statuses and separate `PASS / FAIL / NOT TESTED` results. Record the specific validation method. An import error, failure to launch, or unavailable visual inspection does not count as success. If a check cannot be performed, explicitly state the limitation.

The new names, numerical budgets, and dimensions below are **project guidelines for this test**, not statements about the internal implementation of the reference games or universal industry standards.

## 1. System content

Create one original system: a star and **three fully landable planets**. They must differ not only in color but also in terrain, atmosphere, lighting, vegetation/geology, and points of interest. For example: rocky and arid, green with bodies of water, cold or volcanic. Choose the specific names and art direction yourself.

Each of the three planets must be approachable from different directions, with landings possible at different suitable locations, not just one story-designated spot. The star is not a landable object. Distinguish decorative distant stars from accessible objects through navigation. A gas giant, moons, a station, and asteroids are acceptable after the main loop is complete, but not instead of the third working planet.

Use **compressed gameplay scales**, not real astronomical distances. Initial guideline: planet radii on the order of 2–6 km, with distances between centers of tens of kilometers and enough separation to prevent atmospheres from intersecting. Tune speeds so that a selected interplanetary trip takes approximately 30–90 seconds, and entering/leaving the atmosphere is a visible process. Record the final values. Do not shrink the ship to a dot or make a single character step hundreds of meters long to fake scale.

Do not implement an infinite galaxy, story campaign, multiplayer, economy, hundreds of animal species, or complex crafting. None of these should take time away from seamless travel.

## 2. A unified world and coordinates

First choose and describe a robust coordinate architecture. Separate logical system positions from local rendering/physics coordinates. If necessary, store logical coordinates in double precision and shift the local origin around the player.

Origin shifting is a technical transformation, not teleportation within the game world: preserve the relative positions of planets, the ship, camera, particles, landmarks, and velocities. Prevent jerks, camera jitter, and loss of saved beacons. Do not join incompatible scene scales without a mathematically consistent transition.

On the surface, the downward direction is defined relative to the center of the corresponding planet. Do not use a single world vertical for all planets. For this test, keeping planet centers stationary is acceptable; complex orbital/N-body simulation is not required. Daylight can be changed separately. Transitions between planets' spheres of influence must use hysteresis and must not flip back and forth near a boundary.

The ship and camera must retain control and understandable orientation when moving between modes. Collisions, altitude, and navigation must use one consistent coordinate system.

## 3. Planet geometry and background data

Create procedural spherical surfaces: a cubed-sphere with faces divided into patches, quadtree LOD, or another justified implementation. This is a technical option, not a requirement to use a particular library.

Each planet must have a seed and a single terrain function based on direction/coordinates. The distant silhouette, nearby surface, and physical elevation must describe the same planet. Do not replace a continent visible from orbit with a different one during landing.

Generate more detail near the player; simplify distant surfaces. Do not generate an entire planet at on-foot detail all at once. Handle patch joins, different LODs, normals, and seams between faces. Use edge matching, stitching/skirts, or another verified technique without visible holes.

Apply a per-frame budget to loading and mesh/collision generation. Keep heavy computation separate from operations on Unity objects where safe. Do not call main-thread APIs from background tasks. First load sufficient coverage, then enable the next detail level; the old working patch must not disappear before the new one is ready.

Colliders are needed locally near the ship and landing site. Prevent falling beneath the surface and divergence between physics and visuals. During fast flight, prepare patches ahead along the direction of travel. `LoadSceneAsync` alone is not proof of seamlessness: assess the actual behavior [S1–S2].

## 4. Ship and controls

Create one finished ship through Blender: hull, cockpit, engines, distinct surfaces, and landing gear. An expressive, cohesive, game-ready result matters more than a set of ten unfinished ships. Save the source, export it, and integrate it into Unity.

Required:
- throttle control, braking, turning, roll, and altitude adjustment/vertical thrust;
- orbital and atmospheric modes with smooth transitions;
- accelerated interplanetary travel that preserves visible movement;
- smoothly limiting accelerated mode near the surface, rather than colliding at interplanetary speed;
- an external camera and cockpit view, switchable without losing control;
- readable inertia, engine vibration/sound, and surface contact;
- a warning about unsafe closing speed and a way to recover after a crash.

Provide accessible controls that do not require orbital-mechanics skills. Assign keys automatically and display them on a help screen. Landing/takeoff controls must not conflict with menus or looking around.

By default, fuel must not cut short demonstrations of the main features. Fuel consumption and repairs are optional late-stage systems.

## 5. Landing and takeoff

The player must approach the surface, reduce speed, choose an acceptable area, and lower the ship. A landing assistant is acceptable if it smoothly aligns the ship and performs visible movement within the actual world. It must not replace the destination with a different scene.

Check the surface under the landing gear, slope, clearance, obstacles, and water depth. Show a clear rejection for an unsuitable area, but do not prevent landing solely because a designated landing pad is absent. The gear and hull must not float a meter above the visible ground or sink into it.

On takeoff, lift the ship from that same surface and restore free control without changing the world. Preserve terrain features and player-placed markers on return visits.

After the loop works across three planets, add the ability to exit the ship and explore on foot: correct local gravity, the ability to walk away, return, and board again. If this cannot be completed, clearly mark it as an additional unfinished feature; do not hide a missing seamless landing behind a small on-foot scene.

## 6. Exploration and visual feedback

Provide a system map/diagram, target selection, planet name, distance, speed, altitude above the local surface, and a flight-mode indicator. Distances must be calculated, not displayed as arbitrary numbers.

On each planet, place several geographical landmarks and at least one original point of interest: a rock arch, crater, ruins, crystal field, small outpost, or another recognizable object. Create the ship and important authored objects in Blender; spheres, terrain, vegetation distribution, and atmospheres can reasonably be generated by the engine.

Implement scanning/marking discoveries and saving a player beacon. This is a lightweight exploration objective, not a separate cumbersome campaign.

Transitions in lighting, sky, atmospheric haze, sound, and cloud layers must be continuous. Do not hide a technical swap behind a black screen, excessively dense clouds, or a fixed video sequence. Do not copy No Man’s Sky music, interface, or assets.

## 7. Validation that can be shown on video

First implement one planet and a reliable landing/takeoff loop; then add the remaining two while maintaining quality. This is the development order, not permission to finish with one planet.

Required tests:
1. A fresh launch starts in space, and the ship is controllable.
2. An uninterrupted route: orbit → surface A → takeoff → surface B → takeoff → surface C.
3. Landing on the day and night sides, at several suitable points on one planet.
4. Fast approach: no passing through the ground, disappearing collisions, or an entire planet appearing too late.
5. Flight across patch joins and different LODs: no holes or noticeable terrain jumps.
6. Returning to a beacon after a long flight; the same terrain and position.
7. Saving and loading in space and on the surface.
8. Repeating several flights: no unbounded growth in patch count or memory usage.

Create a separate testing button/menu: move to the start of the demonstration route, show FPS, active patches, memory, coordinate mode, and reset the test save. Teleportation is allowed **only as an explicitly labeled debug tool**, not as the implementation of normal travel.

Record actual frame times on the available computer and the graphics settings. A practical guideline is 1080p at a stable 30 FPS or higher; 60 FPS is a desired target, not a fabricated guarantee. Measure long frames during transitions too, not just the average.

Leave a ready-to-use startup scene, automatic Prefab/material/input setup, `README_RUN.md`, `FEATURE_MATRIX.md`, Blender sources, and a Windows development build if the installed toolchain supports creating one. Do not open a second Unity Editor on the same folder simultaneously for batch validation; choose a safe automation mode. Screenshots and a report do not replace a working project.

## Sources and reference boundaries

[S1] Unity Mesh API — creating and updating geometry: `https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html`

[S2] Unity SceneManager.LoadSceneAsync — background loading: `https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadSceneAsync.html`

[S3] Official No Man’s Sky description — a reference for continuous exploration, not a requirement to reproduce all its content: `https://www.nomanssky.com/about/`

[S4] Unity, exportable 3D formats: `https://docs.unity3d.com/6000.0/Documentation/Manual/3D-formats.html`

Begin by recording the time, checking the working folder and Blender routing, then create the first genuinely seamless flight.

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
Project: Seamless planetary exploration — Unity + Blender
Blender master file: UnityOpus5.5PlanetGame.blend
Full master-file path:
MCP server actually used:
Blender port: 9876

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
