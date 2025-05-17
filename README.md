# 🎥 Manim Project

## 👥 Authors

- **Code**: Ziyi Liu  
- **Mathematical Concept**: Dr. Anen Lakhal

---

## 📦 Installation

To get started with Manim, please follow the official installation guide:

🔗 [Manim Community Edition – Installation Instructions](https://docs.manim.community/en/stable/installation.html)

This guide provides several installation options, including via `pip`, `conda`, or Docker.

---

## 🧪 Usage

Once Manim is installed, you can create animations by writing Python scripts that define scenes. Each scene is a class that inherits from `Scene` and implements a `construct()` method where you define your animation steps.

Here’s a basic example:

```python
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        square = Square()
        self.play(Create(square))
        self.play(Transform(square, Circle()))
        self.play(FadeOut(square))
```

To render this scene, save the code in a file (e.g., `square_to_circle.py`) and run the following command:

```bash
manim -pql square_to_circle.py SquareToCircle
```

This will render the `SquareToCircle` scene in low quality and preview it automatically.

---

## 📂 Project Structure

```
manim/
├── src/                 # Source code for all Manim scenes
├── .gitignore           # Files and folders ignored by Git
└── README.md            # Project documentation
```

All custom animation scenes are located in the `src/` directory.

---

## 🎞️ Watch on YouTube

📺 Explore our animations here:  
👉 [Ziyi-star0503 YouTube Channel](https://www.youtube.com/@Ziyi-star0503/videos)

---

## 🔧 Contributing

Contributions are highly appreciated! To contribute:

1. Fork this repository.
2. Create a new branch:  
   `git checkout -b feature-name`
3. Make your changes.
4. Commit your work:  
   `git commit -am 'Add new feature'`
5. Push the branch:  
   `git push origin feature-name`
6. Open a Pull Request.

Please ensure your code follows the project’s style and includes necessary tests if applicable.

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for full details.
