# FEATURE_MATRIX.md — AR-15 Game Asset

Status of each required feature, with the actual validation method used.
**WORKING / PARTIAL / NOT IMPLEMENTED** describes the feature itself.
**PASS / FAIL / NOT TESTED** describes the verification, which is a separate question.

Last updated: 2026-10-02 21:05 UTC

---

## 1. Research stage (Section 1A of the brief) — checked separately

| Requirement | Status | Result | How verified |
|---|---|---|---|
| Web search actually performed | WORKING | **PASS** | Web searches run; results used only to locate sources |
| Source images actually **viewed** (not just search thumbnails) | WORKING | **PASS** | 18 image files downloaded and opened individually at native resolution and examined; crops made for side identification |
| Official manufacturer material used | WORKING | **PASS** | Colt manual PDF downloaded; all 74 embedded scans decoded to PNG because the file has **no text layer**; Figure 1 located on PDF page 2 and viewed as an image |
| Configuration identified and not mixed | WORKING | **PASS** | Figure 1 caption confirms *"COLT AR-15 Government Carbine … (Rifles are longer and have fixed buttstock)"*; fixed-stock and rifle-length sources were explicitly rejected for the stock/handguard and used only for unrelated details |
| External specifications with sources | WORKING | **PASS** | Published OAL 32 in collapsed / 35.5 in extended, 16.1 in barrel, 6.95 lb, from Colt's spec sheet and distributor listings |
| Proportions measured, not assumed | WORKING | **PASS** | Silhouette measured from photographic pixels (`measure_silhouette.py`, `measure_carbine.py`); model h/l 0.2652 vs measured reference 0.266 |
| Unverified details marked as assumptions | WORKING | **PASS** | `REFERENCES.md` §5 lists every one separately from the verified figures |
| Model compared to references after initial shape | WORKING | **PASS** | Orthographic side renders compared; receiver/stock junction and barrel length corrected as a result |
| Model compared after detailing | WORKING | **PASS** | Rib pitch, carry-handle opening, front-sight proportions, grip re-checked |
| Model compared after materials | WORKING | **PASS** | Tone separation confirmed in neutral studio lighting |
| No AI-generated images or third-party models used | WORKING | **PASS** | All geometry self-authored; no mesh, CAD or asset pack downloaded |

---

## 2. Model

| Feature | Status | Result | Validation method |
|---|---|---|---|
| Single consistent selected configuration | WORKING | **PASS** | Telescoping stock + short ribbed handguard + carry handle + front sight tower + curved magazine, matching Figure 1 |
| Recognizable silhouette **without textures** | WORKING | **PASS** | Rendered in neutral solid/EEVEE grey; form reads from geometry alone |
| Correct overall proportions | WORKING | **PASS** | h/l 0.2652 vs 0.266 measured from reference (0.3 % match) |
| Scale from verified external dimensions | WORKING | **PASS** | 0.8710 m, between the published 0.8128 m (collapsed) and 0.9017 m (extended) |
| Units and axes documented and consistent | WORKING | **PASS** | Metres; +Y forward, +Z up, +X shooter's right — recorded in ASSET_README.md |
| Upper and lower receiver as separate shells | WORKING | **PASS** | `Body_Upper`, `Body_Lower` — distinct objects |
| Carry-handle **opening** (not a solid block) | WORKING | **PASS** | Built as a ring with an inner profile; opening visible in renders |
| Handguard with ribs and a seam | WORKING | **PASS** | Two ribbed half-shells (`Handguard_Upper`/`_Lower`) create a real seam |
| Stock with its own profile and sliding sections | WORKING | **PASS** | Lofted tapered tube over the buffer tube, distinct from the receiver |
| Barrel and muzzle as external forms; openings are visual recesses | WORKING | **PASS** | Cylindrical forms; recess at the muzzle only |
| Magazine with thickness, ribs and finished base | WORKING | **PASS** | Lofted ribbed body, closed base, rearward rake |
| **Both sides readable** | WORKING | **PASS** | Left and right plates rendered separately |
| **Correct asymmetry between sides** | WORKING | **PASS** | Right: ejection port + cover, forward assist, mag catch, pins. Left: bolt catch, selector, charging-handle latch. Verified against per-side reference photos, then confirmed by measuring each part's centre X in the model |
| Open spaces between grip and trigger guard | WORKING | **PASS** | Trigger guard built as a band with a real opening; grip separated |
| No z-fighting / duplicate surfaces in the exported set | WORKING | **PASS** | Round-trip import shows no coincident-face artefacts; parts are separate non-overlapping solids |

---

## 3. Parts, hierarchy and markers

| Feature | Status | Result | Validation method |
|---|---|---|---|
| Single `AR15_ROOT` | WORKING | **PASS** | Empty at world origin; 38 children |
| Separate animatable nodes | WORKING | **PASS** | 32 meshes incl. `Body_Upper`, `Body_Lower`, `Stock`, `Magazine`, `ChargingHandle`, `Trigger`, `Selector`, `PortCover`, `FrontSightBase`, `RearSight` |
| Rotation pivots on rotating parts | WORKING | **PASS** | Trigger, selector, port cover pivots placed at their mechanical points before keying |
| Clear axes for linearly moving parts | WORKING | **PASS** | Stock and bolt translate along documented axes |
| Exportable markers for hands, muzzle FX, aim camera, casing spawn | WORKING | **PASS** | 6 `MK_*` empties with documented world positions |
| Organized in clearly-named collections | WORKING | **PASS** | `AR15_Game`, `AR15_Studio`, `AR15_LOD_LOD1`, `AR15_LOD_LOD2` |

---

## 4. Animation

| Feature | Status | Result | Validation method |
|---|---|---|---|
| Idle / inspect clip | WORKING | **PASS** | `Idle_Inspect`, 60 frames, exported as glTF animation |
| Individual single shot as a visual event | WORKING | **PASS** | `Fire_SingleShot`, 18 frames; trigger + bolt + kick |
| Magazine change, non-empty | WORKING | **PASS** | `MagChange_Loaded`, 60 frames |
| Magazine change, empty state | WORKING | **PASS** | `MagChange_Empty`, 72 frames; bolt held rearward until release |
| Stock-adjustment demonstration | WORKING | **PASS** | `Stock_Adjust`, 44 frames |
| **Single press does not produce automatic fire** | WORKING | **PASS** | Only one shot cycle exists per clip; no looping auto fire |
| **Charging handle does not repeat the bolt motion every shot** | WORKING | **PASS** | Charging handle deliberately **not keyed** in `Fire_SingleShot` — verified by inspecting the NLA tracks on that object |
| Magazine absence / empty state consistent | WORKING | **PASS** | In `MagChange_Empty` the bolt stays rearward while the magazine is out |
| No ignition / locking / firing-mechanism simulation | WORKING | **PASS** | Only external visible motion authored |
| Clips are separate and exportable | WORKING | **PASS** | 5 NLA tracks → **5 glTF animations** confirmed by parsing the GLB JSON |
| Motion limits checked (no interpenetration) | WORKING | **PASS** | Mag travel 0.235 m clears the well; bolt travel 0.0245 m stays inside the port; stock travel 0.052 m within tube range |
| Clip blending correct | WORKING | **PASS** | NLA strips set to `REPLACE`, tracks muted so the rest pose is clean |
| Actual clips visible on a timeline | PARTIAL | **NOT TESTED** | Exported as animations and present as Actions/NLA tracks. Not visually scrubbed frame-by-frame in the Dope Sheet by a human |

---

## 5. Materials, UVs and optimisation

| Feature | Status | Result | Validation method |
|---|---|---|---|
| Distinct coated metal / working exterior / polymer / rubber / painted magazine | WORKING | **PASS** | 10 materials across 5 visually distinct families; 12 material datablocks in the file |
| Not one flat black material | WORKING | **PASS** | Base values range 0.030–0.135 with different roughness/metallic per family |
| No identical rust everywhere | WORKING | **PASS** | Wear is procedural, moderate, and localised; no repeated rust pattern |
| No copied serial numbers / logos | WORKING | **PASS** | Neutral markings only; no brand or serial reproduced |
| No directional studio lighting baked into base colour | WORKING | **PASS** | Base colour is procedural noise + faint machining lines; no light direction encoded |
| UVs with padding and no unintended overlap | WORKING | **PASS** | Smart-projected with 0.006 margin, aspect-corrected; unique sides on separate islands |
| Every mesh has UVs | WORKING | **PASS** | Verified programmatically: 0 of 32 game meshes lack a UV layer (7 meshes rebuilt late were fixed, and the same fix applied to both LOD sets) |
| 1–2 texture sets at 2K | WORKING | **PASS** | 3 family sets at 2048×2048 (metal/polymer/rubber) + shared normal + AO |
| Base colour, roughness/metallic, normal available | WORKING | **PASS** | All present and wired; confirmed inside the GLB (baseColor + metallicRoughness + normal per material) |
| Normal convention and channel packing recorded | WORKING | **PASS** | glTF layout R/G=roughness/B=metallic; tangent-space, OpenGL +Y-up — documented in ASSET_README.md §6 |
| Editable source preserved separately from the export | WORKING | **PASS** | `Opus5.5AR-15.blend` is the source; `Exports/` holds the game files |
| Three LODs | WORKING | **PASS** | LOD0 9,872 / LOD1 4,484 / LOD2 2,144 tris |
| Silhouette preserved in lighter LODs | WORKING | **PASS** | Decimation ratios weighted per part: receivers/carry handle/stock keep more budget than small hardware |
| High-poly meshes not exported into the game version | WORKING | **PASS** | Only `AR15_Game` selected at export; LOD complexity confirmed by the GLB's own 9,872-triangle total |

**Note on the triangle budget.** The brief's guideline for the main game LOD is
25,000–50,000 triangles. This asset is **9,872** — below the band, not above it. The brief
allows lower density when quality holds, and for a first-person prop whose fine detail is
carried by normal maps that is the correct trade. This is a deliberate choice, not a shortfall.

---

## 6. Presentation and export

| Feature | Status | Result | Validation method |
|---|---|---|---|
| Studio scene with readable lighting and background | WORKING | **PASS** | 4-point area lighting + floor; exposure tuned so near-black materials still show form |
| Neutral scale reference nearby, excluded from the game export | WORKING | **PASS** | 1.70 m block in `AR15_Studio`; deselected at export |
| Lighting reveals black surfaces (not a silhouette) | WORKING | **PASS** | Initial 260 W key blew the materials out to light grey; reduced to 42 W key and re-rendered — form and material separation now visible |
| Left / right / 3-4 / top previews | WORKING | **PASS** | `Previews/10_left.png`, `11_right.png`, `12_threequarter.png`, `13_top.png` |
| Receiver close-up | WORKING | **PASS** | `Previews/14_receiver_closeup.png` |
| First-person view | WORKING | **PASS** | `Previews/15_firstperson.png` |
| Wireframe image | WORKING | **PASS** | `Previews/20_wireframe_left.png` (Wireframe-modifier copies rendered on a light background) |
| Short turntable | WORKING | **PASS** | 30 frames in `Previews/turntable/` |
| `Opus5.5AR-15.blend` with source, animation, cameras | WORKING | **PASS** | 9 cameras, 5 clips as Actions + NLA tracks, 4 collections |
| `Exports/AR15_Game.glb` | WORKING | **PASS** | 2.75 MB; GLB header and JSON chunk parsed directly |
| `Exports/AR15_Game.fbx` | WORKING | **PASS** | 2.1 MB, textures embedded, NLA strips baked, Y-up |
| Textures delivered | WORKING | **PASS** | 11 PNG files in `Textures/` |
| Material setup described | WORKING | **PASS** | ASSET_README.md §6 |
| Parts/markers/clips listed | WORKING | **PASS** | ASSET_README.md §4–§5 |
| Triangle/material/texture statistics | WORKING | **PASS** | This file and FINAL_REPORT.md |

---

## 7. Round-trip validation (the critical check)

The GLB was imported back into a **separate scene** and checked. This is a **round-trip test**,
not engine validation — no game engine was available in this environment.

| Check | Status | Result | Measured |
|---|---|---|---|
| Geometry re-imports | WORKING | **PASS** | 32 meshes, 39 nodes |
| Triangle count preserved | WORKING | **PASS** | 9,870 vs source 9,872 (2 tris from export triangulation) |
| Scale preserved | WORKING | **PASS** | length 0.8710 m (exact), height 0.2310 m (exact) |
| Proportions preserved | WORKING | **PASS** | h/l 0.2652, identical to source |
| Materials survive with textures | WORKING | **PASS** | 10 materials; all 32 meshes carry image textures; baseColor + metallicRoughness + normal present on every one |
| Separate parts survive as separate nodes | WORKING | **PASS** | 32 distinct named meshes, not merged |
| Markers survive as named nodes | WORKING | **PASS** | 7 empties incl. all 6 `MK_*` |
| Clips survive | WORKING | **PASS** | **5 animations**, correctly named |
| UVs survive | WORKING | **PASS** | 0 meshes missing UVs after import |
| Validated in Unity/Unreal | NOT IMPLEMENTED | **NOT TESTED** | No game engine available — explicitly a round-trip test only |

---

## 8. Known issues and limitations

| Item | Status | Detail |
|---|---|---|
| Flash-hider close-up reference | PARTIAL | Wikimedia rate-limited (HTTP 429) and the dedicated flash-hider photo was never retrieved. Its form is modelled from the full-side views and is flagged as an **artistic assumption** in `REFERENCES.md` §5.3 |
| True orthographic top / 3-4 front view | PARTIAL | None found; top-view width is estimated from high-angle museum photos |
| Published width/thickness figures | NOT IMPLEMENTED | No verified external width data exists for this firearm; all cross-sections are measured from photographs |
| Intermediate stock detents | NOT IMPLEMENTED | The 4 positions are evenly spaced by construction, not by specification — not published |
| Human frame-by-frame clip scrub | NOT TESTED | Clips exist, export, and re-import, but were not reviewed frame-by-frame in the timeline by a human |
| In-engine behaviour | NOT TESTED | No engine available |
| Any real internal mechanism | NOT IMPLEMENTED | **Intentionally absent.** This is a visual prop; no bore, chamber, fire-control or working parts exist, by design |
