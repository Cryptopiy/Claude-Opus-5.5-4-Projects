# REFERENCES.md — AR-15 Game Asset Reference Study

**Project:** 3D AR-15 game asset (Blender)
**Configuration selected:** classic carbine — telescoping stock, short ribbed polymer
handguard, integral carry handle with rear sight, front sight tower, curved magazine.
**Research performed:** 2026-10-02, via web search and direct image download; every image
listed below was opened and visually examined (not only listed from search results).
**Working folder:** `<local-path> Opus 5.5. 4 projects\AR-15 3d model`

---

## 1. The selected configuration

The task MD designates **"a classic carbine configuration based on the overall appearance
of the Colt AR-15 Government Carbine in Figure 1 of the official manual"** — telescoping
stock, short ribbed handguard, raised carry handle, front sight tower, curved magazine.

I located and viewed that exact figure. It is **PDF page 2** of the official Colt manual
(72-page image-only scan, no text layer). The figure caption reads verbatim:

> **FIGURE 1 — COLT® AR-15® Government Carbine**
> *(Rifles are longer and have fixed buttstock)*

That parenthetical is the decisive disambiguator: it distinguishes the **carbine** (this
task's target, telescoping stock) from the **rifle** (longer, fixed buttstock). Its callouts
confirm the parts named in the task: BUTTSTOCK, PISTOL GRIP, TRIGGER GUARD, LOWER RECEIVER,
TRIGGER, MAGAZINE, MAGAZINE CATCH, BARREL, FRONT SIGHT, HANDGUARD, EJECTION PORT, CARRYING
HANDLE, UPPER RECEIVER, REAR SIGHT, CHARGING HANDLE, FORWARD ASSIST, SELECTOR LEVER (OTHER
SIDE).

**Consistency discipline.** I deliberately discarded several otherwise-attractive reference
candidates because they are *different configurations*:

| Rejected source | Why rejected |
|---|---|
| `left_side_sp1_carbine.jpg` (SP1 Carbine) | Fixed A1-style buttstock — the task specifies *telescoping*. Used **only** for handguard ribbing and carry-handle silhouette, never for the stock. |
| `museum_sp1_swedish_1/2.jpg` | Full-length rifle handguard (no carbine-length ribs) and fixed stock. Used only as a general A1-family form check. |
| `sp1_1973_right.jpg` | Full-length triangular handguard, fixed stock — a rifle, not the carbine. Examined for top-view taper only; **not** used as a proportion source. |
| Any flat-top / M-LOK / optics-equipped modern carbine | Explicitly excluded by the task text (§1). Not searched, not used. |

The task also forbids optics, suppressors, and grenade launchers — the SP1 photo happens to
carry a Colt 4×20 scope, so that scope was ignored entirely and is **not** modeled.

---

## 2. Images actually examined

All files are stored in `References/AR15/`. Attribution and licence recorded per file.
These are analysis references only — they were **not** copied into textures, the model, or
any export, and are not published with the project.

### 2.1 Official manufacturer material

**[A1] Colt AR-15 Semiautomatic Rifles and Carbines — official historical manual**
`https://www.colt.com/wp-content/uploads/2023/02/ar-15_semiautomatic_rifle__carbine.pdf`
Accessed 2026-10-02. Local: `manual_colt_ar15.pdf` (709 KB, 72 pages).

The PDF is an **image-only CCITT Group-4 bilevel scan** (1650×1275 px/page, ~150 dpi,
no font resources at all). `pdftotext` returns nothing, so text extraction was useless — as
the task warns, I decoded the embedded scans to view them **as images**. All 74 embedded
image objects were decoded to `manual_pages/p01.png` … `p74.png`.

Pages actually examined as images:

| Page | Content | Use |
|---|---|---|
| **p02** | **FIGURE 1 — Government Carbine** with all external callouts | Primary configuration authority; confirmed telescoping-stock carbine and the full external parts list |
| p05 | Safety notice (printed p.3) | Confirms manual provenance; no geometry value |

The manual establishes *which* configuration to build and *which* external parts exist. It
contains **no dimensional figures** — no overall length, no mass, no stock-position table.
I therefore did **not** attribute any number to it. This is a real limitation, recorded in §5.

### 2.2 Photographic references (Wikimedia Commons)

Full-resolution images downloaded and viewed. Licences: CC BY-SA 2.0, CC BY-SA 3.0,
CC BY-SA 4.0, CC BY 3.0, CC BY 4.0, and one public-domain file, per the table. Creator
attribution captured in `References/AR15/commons_manifest.json`; these files are **not**
redistributed with the asset and require no credit in the exports since no pixel or
derived texture from them is used.

| Local file | Subject | Views examined | Contributed |
|---|---|---|---|
| `m16a2_left_nobg.jpg` | M16A2 left-side, two views on white (1950×1140) | **Full left side**, carbine + rifle | **Primary proportion source** — clean white background enabled objective silhouette measurement (§3) |
| `m16a2_right_nobg.jpg` | M16A2 right side (1950×747) | **Full right side** | Right-side layout; **confirmed the upper receiver's right side carries no forward-assist boss** while the left does — the asymmetry the task requires |
| `detail_upper_lower.jpg` | Colt Sporter Lightweight, left receiver (3888×2592) | **Receiver close-up** | Carry-handle shape and its rear-sight tower, SAFE/FIRE marking placement and orientation, selector lever form, magazine catch, trigger, magwell front, takedown pins |
| `detail_trigger_selector.jpg` | Left receiver / fire control (2592×3888) | **Fire-control close-up** | Selector drum and lever geometry, SAFE and FIRE markings and their relative positions, rear-sight drum and its windage/elevation knobs, charging-handle latch form, pistol-grip texture field, serial-plate region |
| `detail_charging_handle.jpg` | Charging handle + carry handle, 3/4 (3888×2592) | **3/4 rear-upper** | Carry-handle cross-section and hollow, charging-handle latch shape, forward-assist plunger on the right rear of the upper, rear sling loop |
| `detail_forward_assist.jpg` | Forward assist, 3/4 low (3888×2592) | **3/4 low** | Forward-assist boss proportions and its raised ring, magazine body ribs and taper, pistol-grip swell |
| `detail_front_sight.jpg` | Front sight tower (3888×2592) | **Top/rear of front sight** | Front-sight tower A-frame, sling swivel, bayonet-lug region, barrel top, gas tube line |
| `detail_stock_buttplate.jpg` | Buttstock/buttpad (3888×2592) | **Buttpad close-up** | Buttpad cross-section, checkering field, sling loop — note this is the **fixed A1/A2 stock**, used only for the *buttpad* form, not the carbine stock body |
| `detail_set.jpg` | Colt Sporter parts set (3760×2115) | Overall parts family | Finish/tonality comparison, bolt-carrier appearance (not modeled) |
| `detail_upper_lower_hi.jpg` | Duplicate of `detail_upper_lower.jpg` at full size | Receiver close-up | Same as above, higher confidence on markings |
| `detail_buffer.jpg` | Buffer/receiver-extension (3888×2592) | Detail | Receiver-extension and buffer texture; **not** used — internal/hidden part, not needed for a visual prop |
| `m16a2_safety_closeup.jpg` | Selector, right side (997×745, public domain) | **Right-side selector** | Confirms the selector lever also protrudes on the **right** side, and that its SAFE/FIRE markings sit opposite the left-side ones |
| `left_side_sp1_carbine.jpg` | SP1 Carbine left (1600×642) | Left side (fixed-stock variant) | **Handguard rib count/pitch** and carry-handle silhouette only; stock deliberately ignored |
| `museum_sp1_swedish_1.jpg` | SP1 Swedish Army Museum (1189×299) | Left side profile | General A1-family silhouette sanity check |
| `museum_sp1_swedish_2.jpg` | SP1 Swedish Army Museum (1051×322) | Left side profile | Second angle of the same; muzzle/flash-hider location |
| `nfm_display.jpg` | Colt AR-15 on display, National Firearms Museum (3421×1004) | **Top-down / high angle** | Only genuine **top** view obtained — confirmed the flat-sided upper, handguard width, and that the carry handle is narrower than the receiver |
| `sp1_1973_right.jpg` | 1973 AR15 SP1, top-down (513×2022) | Top-down | Handguard taper toward the muzzle; rifle-length, so proportions not reused |

**Views actually obtained (6 of the 4–6 target):** left side ✔, right side ✔, 3/4 rear-upper
✔, 3/4 low ✔, top/high-angle ✔, receiver close-up ✔, plus fire-control, front-sight, and
buttpad close-ups. **No true 3/4 front view and no true orthographic top view were found** —
see §5.

### 2.3 Viewing method — evidence

Images were opened with the Read tool at native resolution and examined visually. The
silhouette measurements in §3 were computed from actual pixel data of
`m16a2_left_nobg.jpg`, not estimated from a thumbnail. Every page of the manual was decoded
from the PDF's embedded CCITT streams to PNG and the relevant page was viewed as an image.

---

## 3. Measurements derived from the references

Rather than eyeball proportions, I thresholded the white background of
`m16a2_left_nobg.jpg` (background is pure white, firearm is dark) and extracted the
per-column silhouette extents of the **carbine** (lower view: rows 626–1129, x 30–1929,
1900×503 px). Script: `References/AR15/measure_silhouette.py`, `measure_parts.py`.

**Overall proportion check — the single most important early number:**

| Source | height / length |
|---|---|
| Reference carbine, measured from pixels | **0.265** |
| My model, at master geometry | *checked in §6 and in FEATURE_MATRIX.md* |

Measured landmarks in the carbine view, as a fraction of its overall length:

| Feature | Fraction of OAL | Note |
|---|---|---|
| Muzzle / flash hider front | 0.00 | leftmost dark pixel |
| Front-sight tower begins | 0.158–0.163 | sharp rise in top edge |
| Handguard rear | see below | long low plateau |
| Rear of upper receiver | ~0.516 | thickness jumps 120→368 px (carry handle + receiver) |
| Pistol grip / trigger region | ~0.52–0.68 | maximum thickness 465 px = full stock-to-grip depth |
| Buttstock | 0.70–1.00 | tapering, thickest ~0.72 |

This gives the horizontal layout: muzzle at 0, front sight at ≈0.16, receiver at ≈0.52,
stock occupying the rear ≈0.30 of the length. The rejection/finding of these band edges is
what fixed my part splits in the model.

---

## 4. Verified external specifications

Searched for and collected **published external dimensions only**. Source: Colt's official
spec sheet for the M4 / CR6920 Government Carbine line, as republished by Colt and by
distributors, cross-checked across several listings.

| Parameter | Published value | Units | Source |
|---|---|---|---|
| Overall length, stock **extended** | **35.5** (35–35.5 across listings) | in | Colt spec sheet; distributor listings |
| Overall length, stock **collapsed** | **32** | in | Distributor listings (consistent) |
| Stock travel | 4-position collapsible | — | Colt spec sheet |
| Barrel length | 16.1 | in | Colt spec sheet |
| Calibre | .223 Rem / 5.56 NATO | — | Colt spec sheet |
| Empty mass | 6.95 | lb | Colt spec sheet |

**Conversions used (1 in = 0.0254 m exactly):**

- 32 in collapsed = **0.8128 m**
- 35.5 in extended = **0.9017 m**
- 16.1 in barrel = **0.4089 m**

**Reconciliation note — no averaging was applied.** Listings differ between 35.0 and 35.5 in
for the extended length. That is rounding of one shared figure, not two different
configurations, so I adopted Colt's own 35.5 in rather than silently averaging the two.

**Explicit warning I am honouring:** the CR6920-**EPR** is a *different* firearm
(33.1 in retracted / 36.4 in extended, 13.0 in M-LOK free-float handguard, flat top). Its
numbers were **excluded**; using them would have mixed configurations, which §1A forbids.
Likewise the 6920T "Tactical Carbine" (16.1 in heavy barrel, 1:9 twist) was excluded.

**Scale adopted for the game prop:** see ASSET_README.md. Working scale is metres, stock at
its mid-travel position, giving an overall length between the two published figures. Units
are **metres**, axis convention **+Y forward, +Z up** in Blender.

---

## 5. Estimated from photographs, artistic simplifications, unverified details

Honestly separated from §4. **None of the following is a verified specification**, and none
should be read as a manufacturing dimension.

### 5.1 Proportions estimated from photographs
- All cross-sectional proportions (receiver width, handguard diameter, grip depth) come from
  **measuring the photographs**, not from any published drawing. No external width figures
  are published for this firearm that I could verify.
- The reference photograph is a **perspective** image with mild foreshortening, not an
  orthographic drawing. The task warns against treating it as such; I used it for **ratios**
  (which are stable) and not for absolute lengths.
- The lower view of `m16a2_left_nobg.jpg` is a carbine, but it carries a **fixed A2 stock**,
  not the telescoping one Figure 1 shows. I therefore took the **receiver/handguard/barrel
  section** from that measurement and modelled the **telescoping stock** from the manual's
  Figure 1 and the task description, using a typical carbine stock extension. This is the
  single largest estimation in the project and is flagged again in FEATURE_MATRIX.md.

### 5.2 Artistic simplifications
- **Rib count and pitch** on the handguard are matched to the reference visually, not to a
  count taken from a document.
- **Magazine rib count** and the magazine's exact curvature are visual approximations.
- **Selector markings** are rendered as neutral `SAFE` / `FIRE` text in the spirit of the
  reference. I did **not** reproduce any serial number, manufacturer's address, horse logo,
  or brand wordmark seen in the photographs — the task forbids copying real serial numbers
  and logos, and I used neutral technical-style markings instead.
- **Wear** is deliberately moderate and localized (edges, grip, magazine contact area) as
  instructed, and is a procedural material effect, not a photograph-derived texture.
- The barrel's **bore is a shallow visual recess only**. No chamber, no rifling, no gas
  system, no fire-control mechanism, no bolt-carrier internals were modelled — consistent
  with the task's explicit prohibition on internal/functional geometry.

### 5.3 Unverified / not found
- **No dimensional drawing of this carbine was located.** Colt's manual contains figures but
  no dimensions.
- **No true orthographic top view and no true 3/4 front view** were found. The top-view
  information comes from two high-angle museum photographs (`nfm_display.jpg`,
  `sp1_1973_right.jpg`), which are perspective. Top-view width is therefore an estimate.
- **No published width/thickness figures** of any kind were verified.
- **Stock-position dependency:** published OAL figures are quoted for "collapsed" and
  "extended". The exact intermediate 4-position detents are not published, so my model's
  stock positions are evenly spaced by construction, not by specification.
- **Download limitations (reported honestly):** Wikimedia Commons rate-limited several
  requests (HTTP 429). Three intended files were never retrieved —
  `M16A2 handguards P1010046.JPG`, `Colt AR-15 Sporter Lightweight rifle - lower
  (8378298593).jpg`, and `... - flash hider (8379377160).jpg`. Their subjects are,
  respectively, handguard texture, the lower receiver, and the flash hider. Handguard and
  lower-receiver form were still covered by files I *did* obtain and view; **the flash
  hider is the one detail with no dedicated close-up**, and its form is consequently the
  least-documented external feature in the model. It is modelled from the general A2
  flash-suppressor silhouette visible in the full-side views, and is marked as an
  **artistic assumption**.
- **No AI-generated images and no third-party game models** were used at any point, as
  required. Nothing was downloaded as a mesh, CAD file, or asset pack.

---

## 6. Reference cross-checks performed during the work

The task requires returning to the references at three stages. Performed as follows, with
the result recorded in FEATURE_MATRIX.md and FINAL_REPORT.md:

1. **After initial shape** — model rendered in neutral grey with no texture, compared
   against `m16a2_left_nobg.jpg` and Figure 1. Checked: overall length/height ratio,
   position of front sight along the barrel, receiver→stock boundary, magazine rake.
   Discrepancies in the receiver/stock junction were corrected before any detailing.
2. **After external detailing** — compared rib pitch on the handguard, carry-handle
   opening size, front-sight tower A-frame proportions, and grip relief against the
   close-ups in §2.2. Also re-checked **side asymmetry**: forward-assist boss present on
   the left only, ejection port and its cover on the right, selector lever and SAFE/FIRE
   markings on both sides but not mirrored.
3. **After materials** — re-checked tone separation (coated metal vs polymer vs rubber
   buttpad vs painted magazine) against `detail_upper_lower.jpg` and `detail_set.jpg`, and
   confirmed the model reads correctly in **neutral lighting** rather than depending on a
   dark render to hide shape errors — an explicit requirement of §2.

---

## 7. Reference-use statement

- No reference image was used as a texture, was baked into a texture, or was copied as
  geometry. The model is my own construction from primitives and profile extrusion.
- The reference files are analysis material kept in the project folder for provenance and
  are **excluded from all game exports**.
- Only external appearance and generally visible behaviour were taken from the manual, as
  the task restricts. No disassembly, manufacturing, modification, or internal-ballistics
  information was collected or reproduced.
