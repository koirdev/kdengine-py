[kdengine-py](https://github.com/koirdev/kdengine-py/tree/main#kdengine-py)

[Libraries](https://github.com/koirdev/kdengine-py/tree/main#libraries)

[Building to *.exe](https://github.com/koirdev/kdengine-py/tree/main#building-to-exe)

[License(s)](https://github.com/koirdev/kdengine-py/tree/main#licenses)

---

[Demo game](https://github.com/koirdev/kdengine-py/tree/main#demo-game)

# kdengine-py
A game engine based on [Shirraria](https://github.com/koirdev/Shirraria)'s source code.

> [!IMPORTANT]
> This project is frozen due to concerns about blocking python.org and pypi.org in Russia.
> 
> This build is not optimized and may be unstable.
>
> This project is being developed for interest and may stop receiving updates in the future. This project was developed for educational purposes only, and its use is not recommended.
>
> The documentation will be updated in the future.
> 

# Libraries
```pip install pypresence``` - pypresence (Discord Rich Presence).

```pip install pygame==2.5.2``` - pygame (Recommended to use 2.5.2 ver.).

```pip install Pymem``` - Pymem.

```pip install PyQt5``` - PyQt5 (Qt5 for Python).

```pip install pillow``` - Pillow.

```pip install pyinstaller``` - PyInstaller, needs for building project into *.exe file.

# Building to *.exe

> [!WARNING]
> Building the project to *.exe is unstable and incorrect! Please keep this in mind before attempting this.
> 

1. ```pyinstaller --debug all --distpath win_build -n shirraria main.py```

3. After that, copy 'assets' and 'kdengine' folders into 'win_build/shirraria/' directory.

# License(s)

The project is distributed under the [**MIT** License](LICENSE).

---

# Demo game

The game ForkMania (A fork of Shirraria) is used as a demo project for the engine.

