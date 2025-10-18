# LAN_ITQ_kisbead

## Leírás
Ez a ROS2 Python package (`teki_rajzolo_pkg`) a TurtleSim-ben képes kirajzolni három előre definiált alakzatot: **triangle**, **square** és **circle**.

A node egyszerűen futtatható, és a felhasználótól bekéri, melyik alakzatot szeretné kirajzoltatni a TurtleSim teknőssel.

---

## Package struktúra
```
-LAN_ITQ_kisbead/
-├── package.xml
-├── setup.py
-└── teki_rajzolo_pkg/
-    ├── __init__.py
-    └── draw_shape_node.py
```

- `teki_rajzolo_pkg` – Python modul(package), tartalmazza a node-ot
- `draw_shape_node.py` – a fő node, ami kirajzolja az alakzatokat

---

## Telepítés és build
1. Klónozd a repository-t:
```bash
cd ~/ros2_ws/src
git clone https://github.com/flmrr99/LAN_ITQ_kisbead.git
```

2. Buildeld a workspace-t:
```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```

---

## Node futtatása

1. Nyiss egy terminált a TurtleSim-hez:
```bash
ros2 run turtlesim turtlesim_node
```

2. Nyiss egy másik terminált a `draw_shape` node futtatásához:
```bash
ros2 run teki_rajzolo_pkg draw_shape
```

3. A program megkérdezi, melyik alakzatot szeretnéd kirajzolni:
```
triangle / square / circle
```

- A TurtleSim teknős kirajzolja a kiválasztott alakzatot

---

## Példaként
- Triangle:
```
-      /\
-     /  \
-    /____\
```

- Square:
```
-  ____
- |    |
- |____|
```

- Circle: folyamatos kör mozgás

---

## Fejlesztő / Kapcsolat
- Fejlesztő: Láng Martin(ITQWMO)
- E-mail: langmartin9999@gmail.com
