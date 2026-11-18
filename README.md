# Claude Opus 5.5 — 4 projects: off-road physics (UE5), space game (Unity), AR-15 game asset and voxel village (Blender)

**[Русский](#русский) · [English](#english)**

---

## Русский

### Claude Opus 5.5 — 4 проекта: off-road физика (UE5), космос (Unity), игровой AR-15 и воксельная деревня (Blender)

Из ролика **«Claude Opus 5.5 — 4 проекта»**: off-road игра Mudtrack на Unreal Engine 5 с деформируемым грунтом, бесшовный космос Sable Reach на Unity, игровая 3D-модель карабина в стиле AR-15 и воксельная деревня Hollowbrook — обе в Blender через Blender MCP.

### Игры

| # | Игра | Движок | Модель ИИ | Скачать / играть |
|---|---|---|---|---|
| 1 | **Mudtrack (Unreal Engine 5)**<br>Off-road про взаимодействие колеса с грунтом: свой C++ полноприводный автомобиль (подвеска, шины, блокировки, лебёдка) на деформируемом грунте с колеями. | Unreal Engine 5.8 | Claude Opus 5.5 | [⬇ Windows](https://github.com/Cryptopiy/Claude-Opus-5.5-4-Projects/releases/download/v1.0/Mudtrack-Unreal-Windows-x64.zip) · [исходники](games/1-mudtrack-unreal) |
| 2 | **Sable Reach — space exploration (Unity)**<br>Бесшовное исследование космоса: перелёты между тремя планетами, вход в атмосферу, посадка и взлёт без загрузок (версия из ролика). | Unity 6000.6.0f1 | Claude Opus 5.5 | [⬇ Windows](https://github.com/Cryptopiy/Claude-Opus-5.5-4-Projects/releases/download/v1.0/SableReach-Unity-Windows-x64.zip) · [исходники](games/2-sable-reach-unity) |
| 3 | **AR-15-style carbine — game asset (Blender)**<br>Игровой нефункциональный 3D-проп карабина: LOD, PBR-текстуры, 5 анимаций, студийные камеры, экспорт FBX/GLB (папка `Exports`). | Blender 5.2 | Claude Opus 5.5 | [исходники](games/3-ar15-game-asset) |
| 4 | **Hollowbrook — voxel village (Blender)**<br>Процедурная воксельная деревня 96×96 м: река, мост, 14 зданий, жители, животные, анимация день/вечер и GLB-модель. | Blender 5.2 | Claude Opus 5.5 | [исходники](games/4-voxel-village) |

### Быстрый старт

- **Готовые сборки для Windows:** в таблице нажмите «⬇ Windows» (или откройте [Releases](../../releases/latest)), распакуйте zip и запустите `.exe` внутри — один файл, установка не нужна.
- **3D-модели:** откройте `.blend` в Blender или возьмите готовые экспорты (FBX/GLB) из папки модели.
- Подробный гайд по запуску и по открытию исходников в движке: **[HOW_TO_PLAY.md](HOW_TO_PLAY.md#русский)**

### Что ещё есть в репозитории

- [BLENDER_MCP_GUIDE.md](BLENDER_MCP_GUIDE.md#русский) — гайд: Claude / Codex + Unity · Godot · Unreal + Blender MCP (PDF: [RU](docs/blender-mcp/Blender_MCP_Guide_RU.pdf), [EN](docs/blender-mcp/Blender_MCP_Guide_EN.pdf))
- [prompts/](prompts) — промпты, по которым ИИ создавал проекты
- [NOTICE.md](NOTICE.md) — товарные знаки, сторонние ресурсы, отказ от ответственности

### Лицензия

Код — **MIT** ([LICENSE](LICENSE)). Собственные ассеты (3D-модели, текстуры, звуки, уровни) — **CC BY 4.0** ([LICENSE-ASSETS.md](LICENSE-ASSETS.md)). Сторонние библиотеки и ресурсы — под своими лицензиями ([NOTICE.md](NOTICE.md)).

> Некоммерческий учебный проект: игры созданы ИИ для YouTube-обзора. Проект не связан с владельцами упомянутых игр, брендов и товарных знаков и не одобрен ими.

---

## English

### Claude Opus 5.5 — 4 projects: off-road physics (UE5), space game (Unity), AR-15 game asset and voxel village (Blender)

From the **“Claude Opus 5.5 — 4 projects”** video: the off-road game Mudtrack in Unreal Engine 5 with deformable soil, the seamless space game Sable Reach in Unity, a game-ready AR-15-style carbine model and the voxel village Hollowbrook — both in Blender via Blender MCP.

### Games

| # | Game | Engine | AI model | Download / play |
|---|---|---|---|---|
| 1 | **Mudtrack (Unreal Engine 5)**<br>Off-road driving about wheel–soil interaction: a custom C++ 4x4 (suspension, tyres, diff locks, winch) on deformable soil that keeps ruts. | Unreal Engine 5.8 | Claude Opus 5.5 | [⬇ Windows](https://github.com/Cryptopiy/Claude-Opus-5.5-4-Projects/releases/download/v1.0/Mudtrack-Unreal-Windows-x64.zip) · [source](games/1-mudtrack-unreal) |
| 2 | **Sable Reach — space exploration (Unity)**<br>Seamless space exploration: fly between three planets, enter the atmosphere, land and take off with no loading screens (video version). | Unity 6000.6.0f1 | Claude Opus 5.5 | [⬇ Windows](https://github.com/Cryptopiy/Claude-Opus-5.5-4-Projects/releases/download/v1.0/SableReach-Unity-Windows-x64.zip) · [source](games/2-sable-reach-unity) |
| 3 | **AR-15-style carbine — game asset (Blender)**<br>Game-ready non-functional carbine prop: LODs, PBR textures, 5 animation clips, studio cameras, FBX/GLB exports (`Exports`). | Blender 5.2 | Claude Opus 5.5 | [source](games/3-ar15-game-asset) |
| 4 | **Hollowbrook — voxel village (Blender)**<br>Procedural 96×96 m voxel village: a river, a bridge, 14 buildings, residents, animals, a day/evening animation and a GLB. | Blender 5.2 | Claude Opus 5.5 | [source](games/4-voxel-village) |

### Quick start

- **Ready-made Windows builds:** click “⬇ Windows” in the table (or open [Releases](../../releases/latest)), unzip and run the `.exe` inside — a single file, no installation.
- **3D models:** open the `.blend` in Blender or use the ready exports (FBX/GLB) from the model folder.
- Detailed run guide and how to open the sources in the engine: **[HOW_TO_PLAY.md](HOW_TO_PLAY.md#english)**

### Also in this repo

- [BLENDER_MCP_GUIDE.md](BLENDER_MCP_GUIDE.md#english) — guide: Claude / Codex + Unity · Godot · Unreal + Blender MCP (PDF: [EN](docs/blender-mcp/Blender_MCP_Guide_EN.pdf), [RU](docs/blender-mcp/Blender_MCP_Guide_RU.pdf))
- [prompts/](prompts) — the prompts the AI used to build the projects
- [NOTICE.md](NOTICE.md) — trademarks, third-party components, disclaimer

### License

Code — **MIT** ([LICENSE](LICENSE)). Original assets (3D models, textures, sounds, levels) — **CC BY 4.0** ([LICENSE-ASSETS.md](LICENSE-ASSETS.md)). Third-party libraries and assets keep their own licenses ([NOTICE.md](NOTICE.md)).

> Non-commercial educational project: the games were made by AI for a YouTube review. It is not affiliated with or endorsed by the owners of any games, brands or trademarks mentioned.
