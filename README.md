# Manim Project

## Autor

- **Code**: Ziyi Liu
- **Mathematical idea**: Dr Anen Lakhal

---

## 📦 Installation

To get started with Manim, follow the installation instructions provided in the official Manim documentation:

- [Manim Community Edition Installation Guide](https://docs.manim.community/en/stable/installation.html)

This guide covers various installation methods, including using pip, conda, and Docker.

---

## 🧪 Usage

After installing Manim, you can render animations by running Python scripts that define scenes. Each scene is a class that inherits from `Scene` and contains a `construct` method where animations are defined.

For example, a simple scene might look like this:

```python
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        square = Square()
        self.play(Create(square))
        self.play(Transform(square, Circle()))
        self.play(FadeOut(square))
```

To render this scene, save the code in a file (e.g., `square_to_circle.py`) and run:

```bash
manim -pql square_to_circle.py SquareToCircle
```

This command renders the `SquareToCircle` scene at low quality and previews the output.

---

## 📂 Project Structure

The repository currently contains the following directories and files:

```
manim/
├── src/                 # Source code for animations
├── .gitignore           # Git ignore file
└── README.md            # Project documentation
```

The `src/` directory is where your Manim scenes are defined.

---

## 🔧 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new Pull Request.

Please ensure that your code adheres to the project's coding standards and includes appropriate tests.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
