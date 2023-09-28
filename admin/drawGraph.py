import svgwrite
from collections import deque
import json


class Cell:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.content = []
        self.kid = set()
        self.parent = set()

    def to_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "kid": list(self.kid),    # Convert set to list for JSON serialization
            "parent": list(self.parent)  # Convert set to list
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Cell object from a dictionary."""
        cell = cls(data["name"], data["url"])
        cell.kid = set(data["kid"])  # Convert list back to set
        cell.parent = set(data["parent"])  # Convert list back to set
        return cell

html_template = """
                <!DOCTYPE html>
                <html>
                <head>
                <meta charset="UTF-8">
                <title>SVG Example</title>
                <style>
                    #svg-container {{
                    width: 100%;
                    height: 100%;
                    overflow: auto;
                    }}
                </style>
                </head>
                <body>
                <div id="svg-container">
                    <svg width="10000" height="10000">
                    {}
                    </svg>
                </div>
                </body>
                </html>
                """

class DrawGraph:
    def __init__(self):
        with open("./cellLib.json", "r") as f:
            data = json.load(f)
            print(data)
            self.dag = {k: Cell.from_dict(v) for k, v in data.items()}

        for e in self.dag.values():
            print([e.name, e.parent, e.kid])

    def bfs (self, root, position):
        queue = deque([self.dag[root]])
        level = -1

        while queue:
            n = len(queue)
            level = level + 1

            for i in range(n):
                node = queue.popleft()
                position[node] = [level, i]

                for kid in node.kid:
                    kid = self.dag[kid]
                    if kid not in position:
                        queue.append(kid)
                        position[kid] = [-1, -1] 

    def drawDAG(self, root, filename):
        position = {}
        self.bfs(root, position)

        elements_num = [0 for _ in range(100)]
        for _, value in position.items():
            elements_num[value[0]] = max(elements_num[value[0]], value[1] + 1)
        elements_num_max = max(elements_num)

        for _, value in position.items():
            value[1] = (elements_num_max * 50) / elements_num[value[0]] * (value[1] + 0.5)
            value[0] = (value[0] + 1) * 300 - 200
        
        # svgwrite
        dwg = svgwrite.Drawing(filename, profile='full')
        dwg.defs.add(dwg.style('a:hover { cursor: pointer; }'))

        self.drawNode(dwg, self.dag[root], position, set([]))

        # 生成 HTML 文件
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_template.format(dwg.tostring()))

    def drawNode(self, dwg, node, position, visited):
        radius = 8

        # Draw the node
        dwg.add(
            dwg.a(href=node.url, target='_blank')
        ).add(
            dwg.circle(center=position[node], r=radius, stroke='red', fill='#FF8888', stroke_width=2)
        )

        # Draw children
        for i, child in enumerate(node.kid):
            child = self.dag[child]
            if (node, child) not in visited:
                visited.add((node, child))
                self.drawEdge(dwg,
                              position[node][0] + radius, position[node][1],
                              position[child][0] - radius, position[child][1])
                self.drawNode(dwg, child, position, visited)

        dwg.add(
            dwg.a(href=node.url, target='_blank')
        ).add(
            dwg.text(node.name, insert=(position[node][0] + radius * 1.5, position[node][1] + radius / 1.25), font_family="Times New Roman", font_size=20, fill="black")
        )

    def drawEdge(self, dwg, x1, y1, x2, y2):
        dwg.add(
            dwg.path(
                d=("M", x1, y1, "C", (x1 + x2) / 2, y1, (x1 + x2) / 2, y2, x2, y2),
                stroke="#8888FF", fill="none", stroke_width=1)
        )
