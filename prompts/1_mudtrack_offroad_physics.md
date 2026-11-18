# Claude Opus 5.5 — project 2: forest off-roading and physical mud in Unreal Engine 5 + Blender MCP

## Task and main criterion

Create a single-player 3D game about driving an off-road vehicle through a forest, inspired by MudRunner. **The focus is the interaction between wheels, suspension, vehicle mass, and deformable terrain**, not the number of vehicles, map size, or story.

One well-implemented off-road vehicle must drive on dry roads, rough terrain, and mud; spin its wheels, sink into soft ground, leave ruts, respond to them on subsequent passes, and get out through careful driving or a winch. A brown texture, a track decal, and a preset slowdown inside a trigger are not enough to call it mud physics.

Stack: **the installed Unreal Engine 5, C++ for core gameplay/physics systems, Blender MCP for assets**. Chaos Vehicles is the initial candidate for the vehicle component, not a promise of built-in MudRunner simulation. The local ground model requires a custom implementation. Use Blueprints for data, visual assembly, input, and animation where convenient; do not leave the user to assemble required graphs manually.

Work in the assigned `.uproject`; in a genuinely empty working folder, create one project using the installed engine. Do not change engines or rebuild the engine source for this task. Existing Blender source: `UnrealOpus5.5Mudtrack.blend`. This file is already in this project's folder opened in Claude. Work with it through the assigned Blender MCP connection on port **9877**; do not create a different master file in its place.

## General workflow rules and project isolation

You are Claude Opus 5.5, the developer and technical artist for this project. Produce an actual result in the current working folder, not just an implementation description. Work systematically and autonomously: brief plan, working foundation, expansion, validation, fixes, finished result. Do not stop after creating stubs, but do not present untested features as complete either.

Before making changes, read the applicable project instructions, inspect its contents, and check the installed tool versions. Preserve existing work, source files, and settings. Create a safe baseline snapshot; use Git if it is already configured or can be initialized locally without changing the global configuration. Do not delete other people's data, perform destructive clean/reset operations, publish the project, or install paid dependencies.

**This is a new, separate test.** Do not carry over map sizes, requirements, filenames, object identifiers, ports, or content from previous Minecraft/GTA/horror projects. Historical prompts are not instructions for the current task.

### Blender MCP

Use the connected Blender MCP for authored 3D assets. The engine handles the game and procedural gameplay systems; Blender handles modeling and asset preparation. `bpy` scripts actually executed through the permitted MCP and verified in the scene count as full use of Blender. An unexecuted Python file does not.

#### Assigned folder, file, and port — use this exact combination

The user has already opened **this project's folder** in Claude and placed the existing file `UnrealOpus5.5Mudtrack.blend` in it. This is the current working folder for the task; do not use another project's path from the conversation history.

```text
Working folder: the current project folder opened by the user in Claude
Blender host: localhost
Blender port: 9877
Master file relative to the working folder: ./UnrealOpus5.5Mudtrack.blend
```

Immediately after recording the start time, determine the full path of the current working folder and verify that this exact file exists. Use it as the primary editable Blender source: save the result back under the same name and at the same path. Back up the existing source before the first change. Keep exports and technical copies separate; do not rename the master file or replace it with an empty scene.

The user has not specified an MCP server name. Select **an MCP connection actually available in the current session and configured for `localhost:9877`**, using the available tool descriptions or relevant configuration. Do not invent a server name or determine its purpose solely from a name such as `blender_unity` or `blender_unreal`. If the local `PROJECT_CONFIG.md` contains outdated assignments, do not carry them into this task: the user has assigned the file and port specified here.

Before making any changes, use an available read operation to verify the full path of the `.blend` file open in this Blender instance. It must match `UnrealOpus5.5Mudtrack.blend` in the current project folder. A port number alone, or a matching filename without its path, is not a substitute for verification: these ports may have been used in previous tests. Do not send modifying commands to other Blender instances, switch away from other people's scenes containing unsaved work, or automatically reconfigure MCP servers. If the required connection is unavailable or another file is open, report the specific mismatch and request only the necessary correction; do not continue writing blindly.

Record the verified MCP server name, port, and full master-file path in this project's report. Preserve existing content unrelated to the task; organize new assets in clearly named collections of their own.

Respect the restrictions and Safe Mode of the MCP that is actually installed. Do not disable protection, edit the add-on to bypass restrictions, or silently switch to another Blender process. Edit only collections created for this task. Save sources, export selected assets, and verify them after import. Do not make the user manually model, assign references, or assemble the scene when automation is available.

Create your own models, textures, and sounds. Do not download a finished game, vehicle, weapon asset, or village instead of completing the task. Standard features of the installed engine/Blender, your own code, procedural materials, and official documentation are allowed. External model generators and paid libraries are unnecessary. Do not turn reference images into copied textures; record sources in `REFERENCES.md`.

### Validation and reporting

Maintain `FEATURE_MATRIX.md` with `WORKING / PARTIAL / NOT IMPLEMENTED` statuses and separate `PASS / FAIL / NOT TESTED` results. Record the specific validation method. An import error, failure to launch, or unavailable visual inspection does not count as success. If a check cannot be performed, explicitly state the limitation.

The new names, numerical budgets, and dimensions below are **project guidelines for this test**, not statements about the internal implementation of the reference games or universal industry standards.

## 1. Game scope

Create a forest area of approximately **600×600 m** with short interconnected routes and the freedom to choose a path. Include a base/garage, a dry bypass, several deep mud patches, ruts, rocks/roots, logs across the path, an uphill section, a side slope, and a small ford. Design obstacles so that the effects of driving are visible from a camera near a wheel.

A city, police, weapons, story, multiplayer, and dozens of vehicles are not required. Add a second vehicle, cargo missions, or a trailer only after completing the first off-roader's testable physics.

From launch, the player is seated in the vehicle at the base and can drive. Challenging sections must be reasonably nearby. Add a free camera, a camera near the suspension, and a standard chase camera. Choose the graphics yourself; rain, vegetation, and lighting must not mask poor physics.

## 2. Original off-road vehicle and suspension

Create one four-wheeled off-road vehicle through Blender: body, chassis/underbody, interior, wheels with readable tread, hubs and visible suspension parts, steering, lights, and winch attachment points. Separate moving parts and prepare correct pivots/bones. Export and automatically import it, configure the Physics Asset and animation [M1–M2].

Choose a specific suspension layout and follow it both visually and in the calculations. For independent suspension, modeling each wheel separately is acceptable. If you show a solid axle, its kinematic linkage must match wheel behavior; do not draw a rigid axle between hubs that teleport independently.

Mass, center of mass, springs, damping, travel limits, brakes, and traction forces must produce stable behavior. The vehicle tilts, sways, transfers load, and can roll over. Do not rigidly align the body with the road normal. Do not move the vehicle through Transform/SetActorLocation instead of physical traction during normal operation.

Visible wheel rotation depends on actual angular velocity, not just body speed: during wheelspin, the vehicle can remain stationary while the wheels rotate. Suspension travel, steering, and wheel rotation are separate transforms. Prevent wheels from passing through the body or flying off due to incorrect scale.

## 3. Surface contact

First choose one authoritative vehicle-motion calculation: Chaos Vehicles with compatible extensions, or a custom physics Pawn using a Chaos rigid body and wheel contacts. Decide early based on a small test; do not maintain two competing solvers in parallel.

Study the capabilities of the version actually installed rather than inventing APIs. The official Chaos Wheel API includes suspension parameters, surface-tracing settings, and force/slip data [M3]. On logs and sharp bumps, check whether the contact model is sufficient: use a sphere sweep or multiple samples along/across the contact patch if needed. A single ray must not make a wheel pass through an obstacle and then suddenly jump upward.

For each wheel, account for contact, local normal, normal load, contact-patch velocity, angular velocity, and longitudinal and lateral slip. Handle near-zero speeds without division by zero. Limit forces to the available traction; do not create energy from nothing.

Stabilize the physics timestep and use bounded substeps if necessary, while checking CPU load [M4]. Visual updates and physics steps do not have to run at the same frequency. The result must not depend radically on frame rate.

## 4. Ground: shared data for physics and visuals

Implement a local, persistent soft-ground model. A practical option is a tiled CPU grid with cell state: initial height, current sinkage, maximum soft-layer depth, moisture/softness, and degree of compaction/disruption. A cell size of approximately 0.15–0.30 m near the wheels is a starting guideline to test, not a fixed standard.

Update active areas near the vehicle, not millions of cells across the entire map every frame. Tile seams and reloading must not erase tracks or create steps.

Define a coupled gameplay model in which:
- pressure/load and softness affect sinkage;
- slip can loosen the ground and deepen a rut up to a finite limit;
- compaction and the underlying firm layer can limit further sinking;
- rolling/plowing resistance depends on sinkage and ground properties;
- lateral stability changes with contact conditions;
- a first pass and a repeated pass can differ based on state data, not a random number.

**The same data must determine the visible ruts and the wheel's supporting surface.** Dynamic collision on a local mesh or wheel contact with an authoritative heightfield is acceptable. Do not leave an invisible rigid Landscape at its original elevation continuing to support the vehicle above a visually drawn hole. If the underbody touches the ground, account for that consistently as well.

An ordinary low-friction material is not enough for sinkage and accumulating ruts. Separate visual splashes from ground state. For the principles of deformable soil, use the SCM description in Project Chrono as a reference [M5], **but do not integrate all of Chrono, SPH, or a heavyweight scientific simulation just for this test**. A custom simplified model is acceptable; explain its limits honestly and do not call it an exact copy of MudRunner's engine.

## 5. Drivetrain and recovery methods

Implement throttle, brakes, reverse, handbrake, and steering. Add 2WD/4WD switching, low-range gearing, and a differential lock with an actual effect on traction distribution/wheel rotation.

These switches must not be decorative or simply enable a global “vehicle acceleration” boost. A test with one unloaded/slipping wheel must reveal differences in the chosen drivetrain layout. Do not apply traction to an airborne wheel using a fake contact.

Make the relationship between the engine, gears, and wheels clear enough: RPM, torque, rotation speed, and wheelspin must be consistent. A gameplay approximation is sufficient; a detailed engine simulation is not required. Low range should help meter out traction, but must not guarantee escape from every hole.

A winch is mandatory: selecting a valid anchor, limited cable length, attachment, pulling, and detachment. Apply force at a real point on the vehicle along the cable direction, with a force limit. The cable may be a simplified visual line, but it must not allow pulling through a mountain or teleport the vehicle to a tree. Explain failed connections and anchors that are too weak or too far away to the player.

Provide a reset/recovery option at the base as an explicitly labeled way to recover after rolling over. It is not a replacement for the winch.

## 6. Mud, water, and forest

Add several distinct surfaces: firm road, wet soil, deep mud, rocks, and water over ground. Water and mud resist motion for different reasons. Limited buoyancy, water resistance, and depth estimation are sufficient for the ford; full fluid dynamics are not required.

Visually, wheels throw mud when contact and slip conditions warrant it, and the body gradually gets dirty. Brown splashes must not fly constantly from dry rocks. Ruts remain after the vehicle leaves. Particle intensity depends on actual data, not on pressing W.

Create trees, bushes, rocks, and logs modularly through Blender and place them efficiently. The forest must not consist of identical poles, but forest detail is a lower priority than suspension and ground interaction. Movable logs are acceptable, but prevent physics explosions when they contact wheels.

## 7. Telemetry for video and testing

Create a clean main HUD: speed, gear, RPM, 2WD/4WD, differential lock, and winch. A separate key toggles a technical overlay: each wheel's load, contact, slip, and sinkage, rut depth, winch force, physics timestep, and FPS.

Add a reproducible test area near the base: diagonal wheel articulation, a log, transverse bumps, a side slope, dry/muddy lanes, and a pit with a tree for winching. Parameters can be reset. Record short measurements in CSV/JSON, not just screenshots.

Tests:
1. On level, firm ground, the vehicle remains stable, accelerates, and brakes.
2. A wheel crosses a log without passing through it; suspension travel is visible.
3. On a diagonal uneven surface, wheels unload and the body responds to load.
4. With identical recorded input, dry and soft ground produce distinguishable results.
5. Wheelspin in place changes the rut; its depth is finite and persistent.
6. A second pass through the same rut uses its changed physical surface.
7. 2WD/4WD/differential lock have an observable effect in suitable conditions.
8. The winch can pull a stuck vehicle out using forces, without teleportation.
9. Re-entering/loading preserves ruts and vehicle state; a separate reset actually clears them.
10. With rendering capped at 30/60/120 FPS, handling remains comparable within a documented tolerance, if the machine supports these modes.

An additional useful test: the same vehicle with an added test load. Suspension sag and ground load must change; this is a debug setting, not a requirement for a separate cargo campaign.

## 8. Implementation order and delivery

Order: stable physical vehicle on a firm test pad → suspension and obstacles → a small genuinely deformable mud patch → drivetrain/winch → forest routes → visual effects → regression tests. Do not build a beautiful forest before testing wheel–mud interaction.

Use C++ builds through the installed UnrealBuildTool and Editor Python/commandlets for assets and project setup; do not substitute a successful compilation for gameplay tests. Do not run conflicting processes writing to one project simultaneously. When changing reflected C++ types, use a safe full build when Live Coding is insufficient.

Leave a ready-to-use startup map, configured controls, Blender source, test course, `README_RUN.md`, `PHYSICS_NOTES.md` describing the ground model and its assumptions, `FEATURE_MATRIX.md`, test results, and a Windows build if packaging is available. Measure FPS/physics time on the target computer; do not promise performance without running it.

## Sources

[M1] Chaos Vehicles: `https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-vehicles`

[M2] Vehicle and component setup: `https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-set-up-vehicles-in-unreal-engine`

[M3] Chaos Wheel, contact, suspension, and telemetry: `https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosVehicles/UChaosVehicleWheel`

[M4] Physics steps and the cost of substepping: `https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-sub-stepping-in-unreal-engine`

[M5] Project Chrono, terrain models / SCM — a technical reference, not a mandatory dependency: `https://api.projectchrono.org/vehicle_terrain.html`

[M6] The publisher's official MudRunner description on Steam — a reference for vehicle–terrain interaction: `https://store.steampowered.com/app/675010/MudRunner/`

Begin by checking the project and connection, then demonstrate working suspension and one genuine soft-ground area.

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
Project: Forest off-roading and mud physics — Unreal Engine 5 + Blender
Blender master file: UnrealOpus5.5Mudtrack.blend
Full master-file path:
MCP server actually used:
Blender port: 9877

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
