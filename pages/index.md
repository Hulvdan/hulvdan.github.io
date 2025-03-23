<p style="text-align: right">
  Switch to <a href="/docs/en.html">English 🇬🇧</a>
</p>

# Алексей Чистов

<p style="text-align: center">
  telegram: <a href="https://t.me/agechistov">@agechistov</a> |
  <a href="mailto:agechistov@gmail.com">agechistov@gmail.com</a>
</p>

<p></p>

Иногда я занимаюсь gamedev проектами. Здесь я собрал о них информацию.

<br>

### Action RPG в разработке

YOUTUBE_LOOP_7QmJfNH99Vg

YOUTUBE__jhTkrgfY14

![](docs/assets/rec2.jpg)
![](docs/assets/rec3.png)
![](docs/assets/rec0.png)
![](docs/assets/rec1.png)

*«Эпос о приключении героя в жанре экшен RPG, где предстоит использовать преимущества и комбинации стихий природы, адаптируя подбор экипировки на пути странствия»*

<br>

### Сокращение Рутины При Разработке

YOUTUBE_5jdQKfxns-4

Демонстрирую техники, которые облегчают мою жизнь разработчика.

<details>
  <summary>
    Раскрыть подробности
  </summary>

**Техники:**

- Сборка и запуск игры по кнопке F5 в редакторе.
- Система записи и воспроизведения действий игрока.
- Горячая перезагрузка кода через DLL.

<p></p>

**Как это облегчает мою жизнь:**

- **Пример 1.** *Кто-то другой играет в мою игру -> она crash-нулась -> я воспроизвожу запись их действий.* Мне не требуются расспросы в духе «что вы нажимали, из-за чего игра crash-нулась?»
- **Пример 2.** *Я сталкиваюсь с багом -> (у меня уже есть запись моих действий) -> из раза в раз запускаю отладчик и игра проигрывает записанные действия автоматически.*
- **Пример 3.** *Мне нужно подредактировать значения в игре -> несколько раз изменяю C++ код и перезагружаю DLL.* Игру перезапускать часто нет необходимости.
- Это не заменяет тесты. Это их дополняет.

<p></p>

**Jonathan Blow и Casey Muratori отмечают важность сокращения времени, затрачиваемого на рутинные действия:**

- Видео. [Handmade Hero Day 023 - Looped Live Code Editing](https://guide.handmadehero.org/code/day023/#2983). Casey Muratori демонстрирует запись и воспроизведение действий игрока, а также горячую перезагрузку DLL.
- Видео. [Jonathan Blow on scripting languages](https://www.youtube.com/watch?v=y2Wmz15aXk0). На фоне Jonathan Blow прогоняет тесты его игры. Это в сущности и есть воспроизведение записи действий игрока.

</details>

<br>

### 3D Демо Перемещения С Помощью Троса - [C++ Source](https://github.com/Hulvdan/shingeki) (2024)

YOUTUBE_X4yfK4Lj8kg

Поработал в 3D, подтянул математику, а также опробовал [Raylib](https://www.raylib.com/). Вдохновлялся Атакой Титанов.

<br>

### 3D Пончик (2024)

![](docs/assets/donut.gif)

Закрепил основы 3D, матричных трансформаций, линейной алгебры и программирования на C++ без использования библиотек.

<br>

### Roads of Horses (10/2023 - 09/2024)

YOUTUBE_aR0MfmgZVeQ

![](docs/assets/tbd4-3.gif)
![](docs/assets/tbd4-4.gif)
![](docs/assets/tbd4-6.gif)

Видеоигра, разрабатывать которую я начал на [Unity, C#](https://github.com/Hulvdan/RoadsOfHorses). После чего начал портировать на [C++](https://github.com/Hulvdan/handmade-cpp-game).
Вдохновленный [Handmade Hero](https://guide.handmadehero.org/), я занимался этим проектом, укрепляя навыки программирования, изучая работу CPU, работу с памятью, рендеринг, аудио и пр.

<br>

<details>
  <summary>
    Раскрыть ещё проекты
  </summary>

### The Clocktower Letter – [itch.io](https://hulvdan.itch.io/the-clockwork-letter) (2023)

![](docs/assets/the_clocktower_letter_first_location.gif)
![](docs/assets/the_clocktower_letter_wall_jumping.gif)
![](docs/assets/the_clocktower_letter_explosion_tower.gif)

Короткая игра платформер для Metroidvania 21 game jam. Я был программистом в распределённой команде из 4-х человек (Unity, C#)

Теперь я понимаю, что можно ожидать от распределённых команд.

<br>

### Остальное (2016-2023)

![](docs/assets/avocado_throwing.gif)
![](docs/assets/avocado_coyote_time.gif)

![](docs/assets/avocado_jump_input_buffering.gif)
![](docs/assets/avocado_camera_shake.gif)

Avocado - [GitHub](https://github.com/Hulvdan/Avocado). Некоторые фишки, применённые к платформеру на Unity, C#.

<p></p>

![](docs/assets/messing_with_see_through_shaders.gif)
![](docs/assets/messing_with_depth_of_field.gif)
![](docs/assets/tanks_ai.gif)
![](docs/assets/piffle_clone.gif)
![](docs/assets/angry_birds.gif)

![](docs/assets/tetris.jpg)
![](docs/assets/pong.gif)

![](docs/assets/2048.jpg)
![](docs/assets/sokoban_in_terminal_block_placed.jpg)
![](docs/assets/sokoban_in_terminal.jpg)

<p></p>

## Credited Work

- [Vanilla Tweaks](https://forums.terraria.org/index.php?threads/vanilla-tweaks-other-little-tweak-mods.37443/#VanillaTweaks) мод для «Terraria» от gardenapple - Поделился кодом для ускорения Extractinator-а (C#) (2017)
- [Run on Save](https://marketplace.visualstudio.com/items/pucelle.run-on-save/changelog) расширение VS Code от pucelle - Исполнение команд VS Code-а при сохранении файлов (TypeScript) (2020)

</details>

<br>

## Другое

### «Dark Souls 3» Cheat Sheet tool – [Reddit](https://www.reddit.com/r/darksouls3/comments/7ylfqp/dark_souls_3_cheat_sheet_tool/) (2018)

![](docs/assets/ds3-cheat-sheet-tool.png)

Программа для ручного отслеживания прогресса в «Dark Souls 3» (Python, PyQt)

<br>

### «Monster Hunter: World» Printable Monsters Weaknesses Booklet – [Reddit post](https://www.reddit.com/r/MonsterHunterWorld/comments/98avyb/mhw_printable_monsters_weaknesses_guide/), [Updated Reddit post](https://www.reddit.com/r/MonsterHunterWorld/comments/njj57i/mhw_printable_monsters_weaknesses_guide_updated/) (2018, 2021)

![](docs/assets/mhw_booklet.jpeg)

Набор изображений/документов для печати, что отображает уязвимости монстров в «Monster Hunter: World» (Python, Pillow)

<br>

## Хотел бы отдать дань уважения

- **[Casey Muratori](https://caseymuratori.com/about)** за серии образовательных стримов [Handmade Hero](https://guide.handmadehero.org/) и образовательных видео [Performance-Aware Programming](https://youtube.com/playlist?list=PLEMXAbCVnmY7t29i_rd3mnALWu-aZr_42&si=e5JxZOPkl09MQK6x)
- **[Jonathan Blow](https://en.wikipedia.org/wiki/Jonathan_Blow)** за его презентации/дискуссии языка программирования [JAI](https://youtube.com/playlist?list=PLmV5I2fxaiCKfxMBrNsU1kgKJXD3PkyxO&si=rX9v9mQwUJyd85x0)

<br>

<p style="text-align: center;">
    (Обновлено 2025-03-14)
</p>
