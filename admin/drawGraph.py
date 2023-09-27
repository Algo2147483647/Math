import svgwrite
from collections import deque
import pickle
import os

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
        with open("html/DAG.pkl", "rb") as f:
            self.dag = pickle.load(f)

    def bfs (self, root, position):
        queue = deque([(root, 0)])
        element = 0
        level_cur = 0

        while queue:
            node, level = queue.popleft()

            if(level != level_cur):
                level_cur = level
                element = 0

            position[node] = [level, element]
            element += 1

            for kid in node.kid:
                if kid not in position:
                    queue.append((kid, level + 1))
                    position[kid] = [-1, -1] 

    def drawTree(self, root, filename):
        position = {}
        self.bfs(self.dag[root], position)

        elements_num = [0 for _ in range(100)]
        for _, value in position.items():
            elements_num[value[0]] = max(elements_num[value[0]], value[1] + 1)
        elements_num_max = max(elements_num)

        for _, value in position.items():
            value[1] = (elements_num_max * 40) / elements_num[value[0]] * (value[1] + 0.5)
            value[0] = (value[0] + 1) * 300
        
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
            dwg.a(
                href='http://localhost:1010/' + node.concept,
                target='_blank'
        )).add(
            dwg.circle(center=position[node], r = radius, stroke='red', fill='white'
        ))

        # Draw children
        for i, child in enumerate(node.kid):
            if (node, child) not in visited:
                visited.add((node, child))
                self.drawEdge(dwg, 
                        position[node][0] + radius, position[node][1], 
                        position[child][0] - radius, position[child][1])
                self.drawNode(dwg, child, position, visited)

        dwg.add(
            dwg.a(
                href=("http://localhost:1010/note/" + node.file if node.file != "" else "ReadMe.md"),
                target='_blank'
        )).add(
            dwg.text(node.concept if node.file != "" else "Math", insert=(position[node][0] + radius * 1.5, position[node][1] + radius / 4 + 4
        )))

    def drawEdge(self, dwg, x1, y1, x2, y2):
        dwg.add(
            dwg.path(
                d = ("M", x1, y1, "C", (x1 + x2) / 2, y1, (x1 + x2) / 2, y2, x2, y2), 
                stroke="blue", fill="none"))
