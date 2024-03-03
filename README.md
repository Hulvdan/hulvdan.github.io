<p style="text-align: right;">Switch to <a href="/docs/en.html">English 🇬🇧</a></p>

# Алексей Чистов

<p style="text-align: center;">
    <a href="mailto:agechistov@gmail.com">agechistov@gmail.com</a>
    |
    <a href="https://www.linkedin.com/in/agechistov">linkedin.com/in/agechistov</a>
    |
    Discord: hulvdan
</p>

<p></p>

Я Python Backend разработчик. В качестве одного из своих хобби я занимаюсь gamedev проектами. Здесь я собрал о них информацию.

## GameDev проекты, над которыми я работал

### Roads of Horses - [C# Source](https://github.com/Hulvdan/RoadsOfHorses), [C++ Port Source](https://github.com/Hulvdan/handmade-cpp-game) <span class="year">(начиная с 10/2023 - н.в.)</span>

{% include youtube aR0MfmgZVeQ %}

![To Be Described](docs/assets/tbd4-3.gif)
![To Be Described](docs/assets/tbd4-4.gif)
![To Be Described](docs/assets/tbd4-6.gif)

Видеоигра, разрабатывать которую я начал на [Unity, C#](https://github.com/Hulvdan/RoadsOfHorses). Сейчас портирую на [C++](https://github.com/Hulvdan/handmade-cpp-game).
Вдохновленный «[Handmade Hero](https://handmadehero.org/faq)», я укрепляю навыки программирования, изучая работу CPU, работу с памятью, рендеринг, аудио, ASM и др.

<p></p>

<details>
    <summary>Из интересного в техническом плане: (кликабельно)</summary>
    <ul>
        <br>
        <li>На C++ я пишу код в основном «от руки», не используя какие-либо фреймворки вроде GLFW / SDL, с целью как можно лучше изучить различные аспекты языка и научиться разрабатывать комплексные вещи.</li>
        <li>Ручная работа с памятью.</li>
        <li>Горячая перезагрузка C++ кода с сохранением состояния при перезагрузках. Я слышал, что при разработке игр очень важно сохранять как можно меньшую длительность итераций.</li>
        <li>По той же причине собираю проект через один юнит трансляции (single translation unit build, unity build).</li>
        <li>Не пытаюсь всё оборачивать в шаблоны, классы и фанатично разделять функции по принципам «Чистого Кода». Сохраняю код максимально простым и прямолинейным.</li>
        <li>Использую clang-tidy и clang-format для сохранения качества и консистентности кода на уровне. Всё же у меня нет коммерческого опыта разработки на C++, поэтому мне очень важно иметь дополнительный «взгляд со стороны».</li>
    </ul>
</details>

### 3D Пончик <span class="year">(2024)</span>

![3D Donut Rotation Animation](docs/assets/donut.gif)

Это я закреплял основы 3D, матричных трансформаций, линейной алгебры и программирования на C++ без использования библиотек.

### The Clocktower Letter – [itch.io](https://hulvdan.itch.io/the-clockwork-letter) <span class="year">(2023)</span>

![The Clocktower Letter - First location](docs/assets/the_clocktower_letter_first_location.gif)
![The Clocktower Letter - Wall Jumping](docs/assets/the_clocktower_letter_wall_jumping.gif)
![The Clocktower Letter - Tower explosion](docs/assets/the_clocktower_letter_explosion_tower.gif)

Короткая игра платформер для Metroidvania 21 game jam. Я был программистом в распределённой команде из 4-х человек (Unity, C#)

### Другие небольшие поделки <span class="year">(2016-2023)</span>

![Avocado - Throwing](docs/assets/avocado_throwing.gif)
![Avocado - Coyote Time](docs/assets/avocado_coyote_time.gif)

![Avocado - Jump Input Buffering](docs/assets/avocado_jump_input_buffering.gif)
![Avocado - Camera Shake](docs/assets/avocado_camera_shake.gif)

Avocado - [GitHub](https://github.com/Hulvdan/Avocado). Некоторые фишки, применённые к платформеру на Unity, C#.

![Messing with see-through shaders inside an isometric Minecraft clone](docs/assets/messing_with_see_through_shaders.gif)
![Messing with a depth of field shader inside an isometric Minecraft clone](docs/assets/messing_with_depth_of_field.gif)
![Tanks AI](docs/assets/tanks_ai.gif)
![Piffle clone](docs/assets/piffle_clone.gif)
![Angry Birds prototype](docs/assets/angry_birds.gif)

![Tetris using C++ w/ cocos2d-x](docs/assets/tetris.jpg)
![Pong](docs/assets/pong.gif)

![2048 using C++ w/ bearlibterminal](docs/assets/2048.jpg)
![Sokoban. Block placed](docs/assets/sokoban_in_terminal_block_placed.jpg)
![Sokoban using C++ w/ bearlibterminal](docs/assets/sokoban_in_terminal.jpg)

## Другое

### Dark Souls 3 Cheat Sheet tool – [Reddit](https://www.reddit.com/r/darksouls3/comments/7ylfqp/dark_souls_3_cheat_sheet_tool/) <span class="year">(2018)</span>

![Dark Souls 3 Cheat Sheet tool](docs/assets/ds3-cheat-sheet-tool.png)

Программа для ручного отслеживания прогресса в Dark Souls 3 (Python, PyQt)

### «Monster Hunter: World» Printable Monsters Weaknesses Booklet – [Reddit post](https://www.reddit.com/r/MonsterHunterWorld/comments/98avyb/mhw_printable_monsters_weaknesses_guide/), [Updated Reddit post](https://www.reddit.com/r/MonsterHunterWorld/comments/njj57i/mhw_printable_monsters_weaknesses_guide_updated/) <span class="year">(2018, 2021)</span>

![Image of a booklet](docs/assets/mhw_booklet.jpeg)

Набор изображений/документов для печати, что отображает уязвимости монстров в игре (Python, Pillow)

## Credited Work

- [Vanilla Tweaks](https://forums.terraria.org/index.php?threads/vanilla-tweaks-other-little-tweak-mods.37443/#VanillaTweaks) мод для Terraria от gardenapple - Поделился кодом для ускорения Extractinator-а (C#) <span class="year">(2017)</span>
- [Run on Save](https://marketplace.visualstudio.com/items/pucelle.run-on-save/changelog) расширение VS Code от pucelle - Исполнение команд VS Code-а при сохранении файлов (TypeScript) <span class="year">(2020)</span>

<br>
<br>

## Хотел бы отдать дань уважения

- <span class="respect">[Jonathan Blow](https://en.wikipedia.org/wiki/Jonathan_Blow)</span> за его презентации языка программирования [JAI](https://youtube.com/playlist?list=PLmV5I2fxaiCKfxMBrNsU1kgKJXD3PkyxO&si=rX9v9mQwUJyd85x0), где он также рассматривает проблемы программирования и того, что с этим можно делать
- <span class="respect">[Casey Muratori](https://caseymuratori.com/about)</span> за его серии образовательных видео [Performance-Aware Programming](https://youtube.com/playlist?list=PLEMXAbCVnmY7t29i_rd3mnALWu-aZr_42&si=e5JxZOPkl09MQK6x) и образовательных стримов [Handmade Hero](https://handmadehero.org/faq)

<br>
<br>

> <div style="text-align: center;">Сие есть моя страница, называемая «GameDev Портфолио».<br>Называть её «Моя страница» будет, вероятно, правильнее.</div>

<p style="text-align: center;">
    (Обновлено {% include today %})
</p>
