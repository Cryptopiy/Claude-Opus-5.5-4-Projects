# How to play / Как запустить

**[Русский](#русский) · [English](#english)**

---

## Русский

### Игры и файлы запуска

- **Mudtrack (Unreal Engine 5)** (Unreal Engine 5.8): [Mudtrack-Unreal-Windows-x64.zip](https://github.com/Cryptopiy/Claude-Opus-5.5-4-Projects/releases/download/v1.0/Mudtrack-Unreal-Windows-x64.zip) → запустите `Mudtrack.exe`
- **Sable Reach — space exploration (Unity)** (Unity 6000.6.0f1): [SableReach-Unity-Windows-x64.zip](https://github.com/Cryptopiy/Claude-Opus-5.5-4-Projects/releases/download/v1.0/SableReach-Unity-Windows-x64.zip) → запустите `SableReach.exe`
- **AR-15-style carbine — game asset (Blender)** (Blender 5.2): только исходники (см. ниже)
- **Hollowbrook — voxel village (Blender)** (Blender 5.2): только исходники (см. ниже)

### Готовая сборка для Windows (1 файл)

1. Скачайте zip игры (ссылка выше или вкладка **Releases** справа на странице репозитория).
2. Нажмите по zip правой кнопкой → **Извлечь всё…** Не запускайте игру прямо из архива.
3. Откройте распакованную папку и дважды кликните `.exe` с названием игры. Всё — установка не нужна.
4. Если Windows показала «Windows защитила ваш компьютер» — это потому, что сборка не подписана платным сертификатом. Нажмите **Подробнее → Выполнить в любом случае**. Исходный код каждой игры лежит в этом репозитории.
5. Проверить, что файл не изменён: в PowerShell выполните `Get-FileHash .\ИмяФайла.zip` и сравните с `SHA256SUMS.txt` в релизе.

Требования: Windows 10/11 64-bit, видеокарта с поддержкой DirectX 12 / Vulkan. Для игр на Unreal Engine при ошибке про отсутствующие DLL установите Microsoft Visual C++ Redistributable (x64) с сайта Microsoft.

### Как открыть исходники в движке

**Unity (6000.6.0f1):** установите Unity Hub и редактор этой версии. **Hub → Add → Add project from disk** → выберите папку игры (где лежат `Assets`, `Packages`, `ProjectSettings`). Первое открытие долгое — Unity создаёт папку `Library`. Откройте основную сцену (см. README игры или `File → Build Profiles`) и нажмите **Play**.

**Unreal Engine (5.8):** установите движок через Epic Games Launcher. Если в проекте есть папка `Source` (C++), нужна Visual Studio 2022 с компонентом «Разработка игр на C++». Дважды кликните `.uproject` и согласитесь пересобрать модули (или ПКМ по `.uproject` → *Generate Visual Studio project files*). Затем **Play** в редакторе.

**Blender:** откройте `.blend` в Blender 4.x/5.x (File → Open). Готовые экспорты (FBX/GLB/OBJ), если есть, лежат в папке `Exports` модели — их можно сразу импортировать в Unity, Godot или Unreal.

### Сделать такую же игру с ИИ

Промпты лежат в папке [prompts/](prompts) (если есть), а гайд по связке Claude/Codex + движок + Blender MCP — в [BLENDER_MCP_GUIDE.md](BLENDER_MCP_GUIDE.md).

---

## English

### Games and launch files

- **Mudtrack (Unreal Engine 5)** (Unreal Engine 5.8): [Mudtrack-Unreal-Windows-x64.zip](https://github.com/Cryptopiy/Claude-Opus-5.5-4-Projects/releases/download/v1.0/Mudtrack-Unreal-Windows-x64.zip) → run `Mudtrack.exe`
- **Sable Reach — space exploration (Unity)** (Unity 6000.6.0f1): [SableReach-Unity-Windows-x64.zip](https://github.com/Cryptopiy/Claude-Opus-5.5-4-Projects/releases/download/v1.0/SableReach-Unity-Windows-x64.zip) → run `SableReach.exe`
- **AR-15-style carbine — game asset (Blender)** (Blender 5.2): source only (see below)
- **Hollowbrook — voxel village (Blender)** (Blender 5.2): source only (see below)

### Ready-made Windows build (1 file)

1. Download the game's zip (link above or the **Releases** tab on the right side of the repo page).
2. Right-click the zip → **Extract All…** Do not run the game from inside the archive.
3. Open the extracted folder and double-click the `.exe` named after the game. That's it — no installation.
4. If Windows shows “Windows protected your PC”, it's because the build isn't signed with a paid certificate. Click **More info → Run anyway**. The full source code of every game is in this repo.
5. To verify the download: in PowerShell run `Get-FileHash .\FileName.zip` and compare with `SHA256SUMS.txt` in the release.

Requirements: Windows 10/11 64-bit, a GPU with DirectX 12 / Vulkan support. For Unreal Engine games, if you get a missing-DLL error, install the Microsoft Visual C++ Redistributable (x64) from Microsoft's website.

### Open the source in the engine

**Unity (6000.6.0f1):** install Unity Hub and that editor version. **Hub → Add → Add project from disk** → pick the game folder (the one with `Assets`, `Packages`, `ProjectSettings`). The first open is slow — Unity rebuilds `Library`. Open the main scene (see the game's README or `File → Build Profiles`) and press **Play**.

**Unreal Engine (5.8):** install the engine via the Epic Games Launcher. If the project has a `Source` folder (C++), you need Visual Studio 2022 with the “Game development with C++” workload. Double-click the `.uproject` and agree to rebuild modules (or right-click it → *Generate Visual Studio project files*). Then press **Play** in the editor.

**Blender:** open the `.blend` in Blender 4.x/5.x (File → Open). Ready exports (FBX/GLB/OBJ), if present, are in the model's `Exports` folder — import them straight into Unity, Godot or Unreal.

### Make a game like this with AI

The prompts are in [prompts/](prompts) (if present), and the Claude/Codex + engine + Blender MCP setup guide is in [BLENDER_MCP_GUIDE.md](BLENDER_MCP_GUIDE.md).
