# FINAL_REPORT.md — AR-15 Game Asset (Blender, project 3)

**Project:** 3D AR-15 game asset — Blender
**Blender master file:** `Opus5.5AR-15.blend`
**Full master-file path:** `<local-path> Opus 5.5. 4 projects\AR-15 3d model\Opus5.5AR-15.blend`
**MCP server actually used:** `custom-blender-ar15` (selected by probing each configured
server's opened file — see §1)
**Blender port:** 9878
**Blender:** 5.2.2 LTS · add-on "MCP for Blender" v1.7 (protocol 7) · **Safe Mode active**

---

## 1. Connection verification (done before any modification)

Four Blender MCP servers were configured. Rather than assume, I read the open file from each:

| MCP server | Port | File it had open | Touched? |
|---|---|---|---|
| `custom-blender-mudtrack` | 9877 | `…\Mudtrack\Mudtrack\UnrealOpus5.5Mudtrack.blend` | **No** — read-only probe only; had unsaved work |
| `custom-blender-planets` | 9876 | `…\Planet Game\Opus5.5PlanetGame.blend` | **No** — read-only probe only |
| `custom-blender-village` | 9879 | `…\Voxel village\Opus5.5VoxelVillage.blend` | **No** — read-only probe only; had unsaved work |
| **`custom-blender-ar15`** | **9878** | **`<local-path> Opus 5.5. 4 projects\AR-15 3d model\Opus5.5AR-15.blend`** | **Yes — this is the correct one** |

The name was determined from the live configuration by reading `bpy.data.filepath` from each
endpoint, not guessed from a name and not carried over from previous tests. Two other
instances hold other people's unsaved work; they were probed read-only and never written to.

**Baseline backup:** `_backup/Opus5.5AR-15_baseline_2026-10-02_2041.blend` — MD5
`eaf7d33250c18a06e70e750115e3a260`, **identical** to the original file at the time of copying.
The original file (`Camera`, `Cube`, `Light`) was preserved and only the default `Cube` removed.

Safe Mode was respected throughout: no attempt was made to disable it, edit the add-on, or
switch to another Blender process. All work was done through `execute_blender_code` plus the
allowed render/export operators.

---

## 2. What was created

A finished, editable, game-ready 3D prop of a **classic carbine AR-15** — telescoping stock,
short ribbed handguard, integral carry handle and rear sight, front sight tower, curved
magazine — matching Figure 1 of Colt's official manual.

**Deliverables:**

| File | Size | Contents |
|---|---|---|
| `Opus5.5AR-15.blend` | — | Source: 32 meshes, 10 materials, UVs, 3 LODs, 5 clips, 9 cameras, studio |
| `Exports/AR15_Game.glb` | 2.75 MB | 32 meshes / 39 nodes / 10 materials / 7 packed images / **5 animations** |
| `Exports/AR15_Game.fbx` | 2.1 MB | Y-up, NLA strips baked, textures embedded |
| `Textures/` | 11 PNG | 3 family base-colour + roughness/metallic sets @2K, shared normal @2K, AO |
| `Previews/` | 10 PNG + 30 frames | left, right, 3/4, top, receiver close-up, first-person, wireframe, turntable |
| `ASSET_README.md` | — | How to open, conventions, parts, markers, clips, materials, exports |
| `REFERENCES.md` | — | Sources, verified specs, and every artistic assumption |
| `FEATURE_MATRIX.md` | — | WORKING/PARTIAL/NOT IMPLEMENTED with PASS/FAIL/NOT TESTED per item |

**Key measured results:**

- Overall length **0.8710 m**, height 0.2310 m, width 0.0564 m
- **height/length = 0.2652** vs **0.266 measured from reference pixels** — a 0.3 % match
- LOD triangles: **9,872 / 4,484 / 2,144**

---

## 3. How to open and use it

1. Open `Opus5.5AR-15.blend` in Blender 5.2+. `AR15_Game` holds the asset; `AR15_Studio`
   holds lights, floor, scale reference and cameras.
2. Cameras: `CAM_Left`, `CAM_Right`, `CAM_ThreeQuarter`, `CAM_Top`, `CAM_Receiver`,
   `CAM_FirstPerson`, `CAM_Turntable`, `CAM_Diag_Rear`, `CAM_Diag_Front`.
3. **Clips** are Actions pushed onto NLA tracks named `Idle_Inspect`, `Fire_SingleShot`,
   `MagChange_Loaded`, `MagChange_Empty`, `Stock_Adjust`. They are muted so the rest pose is
   clean; un-mute a track to play it, or pick the Action by name in the Dope Sheet.
4. **LODs** are in `AR15_LOD_LOD1` / `AR15_LOD_LOD2`, hidden from render by default.
5. Axis convention: **+Y forward (muzzle), +Z up, +X shooter's right**, metres.

---

## 4. Test results

| Test | Result | Detail |
|---|---|---|
| Master-file path verified before modification | **PASS** | Exact path matched; all other instances identified and left untouched |
| Baseline backup created | **PASS** | MD5 identical to original |
| Research performed and images **viewed** | **PASS** | 18 images examined at native resolution; Colt manual's 74 image-only scans decoded and viewed |
| Configuration not mixed | **PASS** | Fixed-stock / rifle-length sources rejected for stock and handguard |
| Silhouette without textures | **PASS** | Renders read correctly in neutral lighting |
| Both sides readable | **PASS** | Left and right plates rendered |
| Side asymmetry correct | **PASS** | Right: port/cover, forward assist, mag catch, pins. Left: bolt catch, selector, charging-handle latch — verified per-side against photos and by measuring centre X |
| UVs on every mesh | **PASS** | 0 of 32 without UVs (7 late-built meshes were found missing and fixed, LODs too) |
| Three LODs | **PASS** | 9,872 / 4,484 / 2,144 tris |
| 5 clips exported | **PASS** | GLB JSON parsed: exactly 5 named animations |
| **Round-trip import** | **PASS** | Into a separate scene: geometry, scale (0.8710 m exact), proportions (0.2652 exact), 10 materials, textures on 32/32 meshes, 32 separate parts, 6 markers, 5 clips, UVs intact |
| Engine validation (Unity/Unreal) | **NOT TESTED** | No engine available — this is a **round-trip test**, not engine validation |

### Defects found and fixed during the work (not hidden)

1. **Lighting blew out the materials** — a 260 W key turned near-black metal light grey.
   Reduced to 42 W; material separation now visible and the model does not rely on darkness.
2. **Fixed-stock reference misidentified** — both guns initially measured were actually *rifles*;
   re-measured against the true carbine and corrected barrel/handguard/grip proportions.
3. **Pistol grip raked forward** instead of rearward — rebuilt.
4. **Sides were swapped** twice during the axis rework — resolved by measuring each part's
   centre X and forcing the verified side.
5. **7 meshes lost their UVs** (rebuilt after the unwrap pass) — found by the round-trip check
   and fixed in the master *and* both LOD sets.
6. **The export was doubled** (64 meshes / 22 materials / 10 animations) because a stale
   `Collection` retained round-trip duplicates that got swept into the export. Found by parsing
   the GLB's own JSON, removed, and re-exported clean.

Point 6 is worth stating plainly: a *successful* export was not a *correct* export, and only
inspecting the file's actual contents caught it.

---

## 5. Limitations

- **No game engine available.** Validation is a Blender round-trip import, explicitly not
  Unity/Unreal validation.
- **Flash hider has no dedicated close-up reference.** Wikimedia rate-limited (HTTP 429) three
  intended images. Its form is modelled from full-side views and is flagged as an artistic
  assumption.
- **No true orthographic top or 3/4-front view exists** in the sources found; top-view width is
  estimated from high-angle museum photographs.
- **No published width/thickness figures** for this firearm were verifiable; all cross-sections
  are measured from photographs, which are perspective, not orthographic.
- **Stock detents are evenly spaced by construction**, not by specification (not published).
- **Clips were not scrubbed frame-by-frame** by a human in the timeline.
- **Deliberately absent:** any internal mechanism, bore, chamber, fire-control parts, or
  manufacturing information. This is a visual prop by design, per the brief.

---

## 6. Time

| | |
|---|---|
| Work started (date, time, timezone) | **2026-10-02 21:40:53 +03:00** (Europe/Moscow, UTC+03:00) — `18:40:53Z` |
| Work ended (date, time, timezone) | **2026-10-02 24:05:29 +03:00** — `21:05:29Z` |
| **Total time spent** | **02:24:36** |
| Total time spent in minutes | **144.6 minutes** |
| Known pauses / resumed segments | One: the session was interrupted after the first MCP probe (before any modification) and resumed when the user fixed the MCP server. No other idle gaps longer than tool round-trips. No parallel operations were summed — this is single-threaded wall-clock |
| Work not included in the measurement | Nothing excluded. All planning, code, Blender work, rendering, importing and testing is inside this window |

Recorded in `.benchmark_runs/project3-ar15/runs/run-2026-10-02/start.json` (start) — see §8 for
the end record.

---

## 7. Tokens and API-equivalent cost

| | |
|---|---|
| **Actual model ID** | `claude-opus-5-5` (as reported in the session's own usage records) |
| Input tokens | **26,261,491** |
| Cache-read tokens | **168,204,961** |
| Cache-write tokens | **1,644,510** |
| Output tokens | **1,051,587** |
| Reasoning tokens | Included in the output figure by the API's accounting; a separate reasoning counter is **not exposed** in this session's usage records |
| **Total tokens (no double-counting)** | **197,162,549** |
| Telemetry source | The session transcript's own per-message `usage` records — 546 of 1,258 entries carry usage. Last observation: **2026-10-02T21:05 UTC** |
| Work not included in the measurement | The final assistant message containing this report is not yet in the transcript when the count was taken |

These are four mutually-exclusive billable categories, so no counter is added twice: input,
cache-write, cache-read and output are disjoint buckets as the API reports them.

### Cost

| | |
|---|---|
| **API-equivalent cost (USD, tokens only)** | **≈ $167.94** |
| Official pricing source, date, and mode | Anthropic first-party API list pricing for `claude-opus-5-5`, consulted 2026-10-02, standard (non-fast) mode |
| Applied rates | Input **$4.00**/MTok · Output **$20.00**/MTok · Cache read **$0.20**/MTok · Cache write **$5.00**/MTok (1.25× input, 5-minute TTL) |

**Formula and arithmetic** (`tokens × rate ÷ 1,000,000`):

| Category | Tokens | Rate | Cost |
|---|---|---|---|
| Input | 26,261,491 | $4.00/MTok | $105.05 |
| Cache write | 1,644,510 | $5.00/MTok | $8.22 |
| Cache read | 168,204,961 | $0.20/MTok | $33.64 |
| Output | 1,051,587 | $20.00/MTok | $21.03 |
| **Total** | | | **$167.94** |

- **Separate external-tool costs:** none. Blender ran locally at no API cost; no paid
  dependency, asset pack or external service was used.
- This is the **token-only API-equivalent** figure. It is **not** a subscription price and not
  an amount billed for this work.

### Accuracy of each result

| Result | Accuracy |
|---|---|
| Total time (02:24:36) | **Measured** — from system clock at start and end |
| Token counts | **Measured** — from the session's own usage records, not estimated from code size or file size |
| Input / output / cache-read cost | **Measured tokens × verified official rate** |
| Cache-write cost | **Estimate** — the standard 1.25× input rate for the 5-minute TTL is applied. If any writes used the 1-hour TTL (2× input, $8.00/MTok), the total would be **≈ $172.87** instead. The TTL mix is not distinguishable in the usage records |
| Reasoning tokens as a separate line | **Unavailable** — not exposed in this session's usage records |
| Per-request attribution of tokens to this task alone | **Not separate** — this session contains only this task (earliest transcript entry `18:40:13Z`, immediately before the recorded start), so the session totals *are* this task's totals; no earlier usage is mixed in |

---

## 8. Completion statement

The brief's completion criteria were checked individually in `FEATURE_MATRIX.md`. The selected
configuration is single and consistent; the silhouette is recognizable without textures; both
sides are readable with correct asymmetry; the magazine and moving parts are separate; UVs
cover every mesh; three LODs exist; materials are separated by family; five clips export and
re-import; and all dependencies live inside the project folder.

The one required check that could **not** be performed is validation in a real game engine —
no engine was available, so the result is reported honestly as a successful **round-trip
import test**, not as engine-validated.
