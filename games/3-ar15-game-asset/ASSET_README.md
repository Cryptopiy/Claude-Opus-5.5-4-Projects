# ASSET_README.md — AR-15 Game Asset

A finished, game-ready 3D prop of a **classic carbine AR-15**, authored from scratch in
Blender 5.2.2 LTS through the Blender MCP connection. Editable source, LODs, materials,
UVs, animation clips, cameras, textures and game exports are all included.

This is a **visual, nonfunctional game prop**. It contains no working mechanism, no bore,
no chamber, and no manufacturing information.

---

## 1. Files

| File | What it is |
|---|---|
| `Opus5.5AR-15.blend` | **Master editable source.** Model, materials, UVs, LODs, 5 clips, studio, cameras. |
| `Exports/AR15_Game.glb` | Game export, glTF 2.0 binary, 2.7 MB. LOD0 + 5 animations + packed textures. |
| `Exports/AR15_Game.fbx` | FBX export (2.1 MB), Y-up, textures embedded. |
| `Textures/` | 2K PNG texture sets (base colour, packed roughness/metallic, normal) + AO. |
| `Previews/` | Rendered PNGs, including `turntable/` (30 frames). |
| `References/AR15/` | Research material (analysis only — **excluded from all exports**). |
| `REFERENCES.md` | Sources, verified specs, and every artistic assumption. |
| `FEATURE_MATRIX.md` | WORKING / PARTIAL / NOT IMPLEMENTED + PASS / FAIL / NOT TESTED. |
| `FINAL_REPORT.md` | Results, limitations, time, tokens, cost. |
| `_backup/` | Untouched baseline snapshot of the original `.blend`. |

---

## 2. How to open

1. Open `Opus5.5AR-15.blend` in Blender (5.2+). The collection `AR15_Game` holds the asset;
   `AR15_Studio` holds lights, floor, scale reference and cameras.
2. Press the numbered camera keys / use the Camera dropdown. Cameras present:
   `CAM_Left`, `CAM_Right`, `CAM_ThreeQuarter`, `CAM_Top`, `CAM_Receiver`,
   `CAM_FirstPerson`, `CAM_Turntable`, `CAM_Diag_Rear`, `CAM_Diag_Front`.
3. **LODs** are in `AR15_LOD_LOD1` and `AR15_LOD_LOD2`. They are hidden from render by
   default so they do not appear in the presentation shots. Un-hide to inspect.
4. **Clips** live as NLA tracks on the animated objects. Open the NLA editor, or use the
   Dope Sheet in Action mode and pick an action by name (see §5).

---

## 3. Scene conventions

| Property | Value |
|---|---|
| Units | **Metres** (Blender metric, scale 1.0) |
| Axes | **+Y = forward (toward muzzle), +Z = up, +X = shooter's right** |
| Overall length | **0.8710 m** |
| Overall height | 0.2310 m (buttpad bottom to the top of the rear sight) |
| Width | 0.0564 m (widest across the selector / pins) |
| height / length | **0.2652** |
| Stock position | mid-travel of the 4-position tube |

**Why these numbers.** Published dimensions for this carbine line are **32 in collapsed** and
**35.5 in extended** (Colt's own spec sheet; see `REFERENCES.md` §4). That is
**0.8128 m … 0.9017 m**. 0.8710 m sits between them, i.e. the stock at mid-travel. The
height/length ratio of 0.2652 was then checked against the carbine silhouette **measured from
photographic pixels** (0.266) — a 0.3 % match. No dimension here is an averaged or invented
figure, and none is a manufacturing tolerance.

The master file's geometry is centred on the origin in Y (spanning −0.4355 … +0.4355) so the
asset rotates cleanly about its midpoint. `AR15_ROOT` sits at the origin.

---

## 4. Parts and markers

32 meshes, organised under a single `AR15_ROOT` empty. Separation is for **game animation**,
not an assembly diagram.

**Receiver / body:** `Body_Upper`, `Body_Lower`, `CarryHandle`, `RearSight`,
`ChargingHandle`, `CH_Latch`

**Barrel group:** `Barrel`, `FlashHider`, `FH_Collar`, `FrontSightBase`, `FSB_Lug`,
`DeltaRing`, `BufferTube`

**Furniture:** `Handguard_Upper`, `Handguard_Lower`, `Stock`, `Buttpad`, `Grip`

**Controls / moving parts:** `Trigger`, `TriggerGuard`, `Selector`, `Magazine`,
`PortCover`, `PortFrame`, `BoltInPort`

**Hardware:** `ForwardAssist`, `MagCatch`, `BoltCatch`, `TakedownPin`, `PivotPin`,
`SlingSwivel`, `SlingSwivel_Front`

**Markers** (empties, attachment points only — not part dimensions):

| Marker | World position (x, y, z) | Purpose |
|---|---|---|
| `MK_Hand_Rear` | (0.000, −0.070, −0.095) | rear hand on the grip |
| `MK_Hand_Front` | (0.000, 0.180, −0.010) | front hand on the handguard |
| `MK_MuzzleFX` | (0.000, 0.443, 0.000) | muzzle flash / smoke origin |
| `MK_CasingSpawn` | (−0.032, 0.190, 0.006) | casing spawn, at the ejection port side |
| `MK_AimCamera` | (0.000, 0.130, 0.055) | aim camera, on the sight line |
| `MK_MagWell` | (0.000, 0.005, −0.072) | magazine socket |

### Side asymmetry — verified, not mirrored

The two sides are deliberately **not** mirror images. Verified against reference photographs
of each side (see `REFERENCES.md` §2.2):

- **Shooter's right (+X):** ejection port and its cover, forward-assist button, magazine
  catch button, takedown and pivot pins, bolt visible inside the port.
- **Shooter's left (−X):** bolt catch paddle, selector lever, charging-handle latch.

---

## 5. Animation clips

Five clips, 30 fps, authored as Actions and pushed onto NLA tracks named after each clip so
glTF exports them as five separate animations. They are **muted** in the scene by default so
the rest pose stays clean.

| Clip | Frames | Contents |
|---|---|---|
| `Idle_Inspect` | 1–60 | slow hold/inspect sway of the whole asset |
| `Fire_SingleShot` | 1–18 | trigger pull, bolt cycling in the port, light upward kick |
| `MagChange_Loaded` | 1–60 | magazine drops and a fresh one goes in |
| `MagChange_Empty` | 1–72 | bolt held to the rear through the change, released only at the end |
| `Stock_Adjust` | 1–44 | stock slides along the buffer tube and returns |

Behaviour deliberately implemented per the brief:

- **A single press produces one shot.** There is no automatic fire.
- **The charging handle is not keyed in `Fire_SingleShot`** — only the simulated bolt moves.
- **`MagChange_Empty` differs from `MagChange_Loaded`** by holding the bolt back; the empty
  state is visually distinct rather than a recolour.
- No ignition, locking or fire-control simulation — this is game-state animation.

Rotating parts have real pivots (trigger at the top of the bow, port cover at its hinge,
selector on its drum); the magazine pivot is at the magwell mouth; the stock translates along
the buffer-tube axis.

---

## 6. Materials and textures

Five visually distinct surface families, not one black material:

| Material | Type | Use |
|---|---|---|
| `M_ReceiverMetal` | coated aluminium | upper, lower, carry handle, rear sight, buffer tube, trigger guard |
| `M_BarrelSteel` | phosphate steel | barrel, front-sight base and lug |
| `M_FlashHider` | steel | flash hider and its collar |
| `M_SmallSteel` | bright steel | pins, selector, charging handle, catches, swivels |
| `M_BoltCarrier` | light steel | bolt face inside the port |
| `M_HandguardPoly` | polymer | ribbed handguard halves |
| `M_GripPoly` | polymer | pistol grip |
| `M_StockPoly` | polymer | stocking body |
| `M_MagPainted` | painted aluminium | magazine |
| `M_ButtpadRubber` | rubber | buttpad (distinctly rougher) |

**Texture sets — one per family (2K, 2048×2048):**

| Family | Base colour | Roughness/Metallic |
|---|---|---|
| METAL | `AR15_METAL_BaseColor_2K.png` | `AR15_METAL_RoughMetal_2K.png` |
| POLYMER | `AR15_POLYMER_BaseColor_2K.png` | `AR15_POLYMER_RoughMetal_2K.png` |
| RUBBER | `AR15_RUBBER_BaseColor_2K.png` | `AR15_RUBBER_RoughMetal_2K.png` |

Plus one shared **normal map** (`AR15_Normal_2K.png`) and one **AO** map
(`AR15_AO_512.png`). An earlier single-set pass produced
`AR15_BaseColor_2K.png` / `AR15_RoughnessMetallic_2K.png`; the per-family sets are the ones
the shaders use and the ones in the exports.

**Channel packing (glTF 2.0 convention), recorded explicitly:** the roughness/metallic map
packs **R = unused, G = roughness, B = metallic** — the glTF metallic-roughness layout, so it
transfers without conversion. Base colour is sRGB; roughness/metallic, normal and AO are
**Non-Color**. The **normal map is tangent-space, OpenGL/+Y-up** — Blender's own convention
and the glTF default. Engines that expect DirectX/−Y-up (some Unreal setups) must **invert
the green channel**; that is a deliberate, documented difference rather than an assumption
that every engine matches.

**Wear** is moderate and procedural — edge and contact break-up plus faint horizontal
machining lines on the metal — not a copied photograph and not uniform rust. All markings are
neutral; **no real serial number, logo or brand wordmark is reproduced.**

Base colour values are deliberately low (0.04–0.13) because anodised aluminium and black
polymer really are near-black. The studio lighting was tuned so that **form reads at those
values** rather than the model relying on a dark render to hide shape errors.

---

## 7. UVs

Smart-projected across all 32 meshes with **0.006 island margin** and consistent texel
density, correcting for aspect. Unique sides are kept apart — the two handguard halves, the
two receivers and the magazine occupy separate islands without overlap. Every mesh has exactly
one UV layer. UVs survive the glTF round trip (verified — see `FEATURE_MATRIX.md`).

---

## 8. Game exports

| Export | Format | Axes | Notes |
|---|---|---|---|
| `AR15_Game.glb` | glTF 2.0 binary | +Y up (glTF convention) | 32 meshes, 39 nodes, **12 materials**, 7 packed PNG images, **5 animations** |
| `AR15_Game.fbx` | FBX binary | Y-up, −Z forward | textures embedded, NLA strips baked |

Axis conversion was applied deliberately at export (`export_yup` for glTF, explicit
`axis_forward='-Z', axis_up='Y'` for FBX) rather than by pre-rotating the asset, so the
authoring scene keeps its documented +Y-forward convention.

**LODs.** Three levels, collapsed with a Decimate modifier and a per-part ratio so
silhouette-critical parts (receivers, carry handle, stock) keep more budget than small
hardware:

| LOD | Triangles | Collection |
|---|---|---|
| LOD0 | **9,872** | `AR15_Game` (exported) |
| LOD1 | **4,484** | `AR15_LOD_LOD1` (≈45 %) |
| LOD2 | **2,144** | `AR15_LOD_LOD2` (≈22 %) |

The brief's guideline for the main game LOD was 25,000–50,000 triangles. At **9,872** this
asset sits *below* that band — deliberately: the target is a first-person prop whose fine
detail is carried by normal maps rather than polygons, and the brief explicitly allows lower
density when quality holds. Only LOD0 and the studio assets are in the exports; the high-poly
working meshes were never exported.

---

## 9. Rendering the presentation

The studio scene renders with **EEVEE** and is ready as-is. Cameras are pre-aimed; the floor
and the 1.70 m scale-reference block sit in `AR15_Studio` and are **excluded from the game
exports** (they were deselected at export time). The scale reference is hidden in the
orthographic technical plates so it cannot intrude on them, and shown in the 3/4 view where
it is useful.

To re-render: set `scene.camera` to a `CAM_*` object and render. Output paths used were
`Previews/`.
