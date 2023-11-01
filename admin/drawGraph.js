let dag = {};

// Load data (assuming it's stored in a file named `dag.json`)
fetch('./admin/cellLib.json').then(response => response.json()).then(data => {
    dag = data;
});

function drawDAG(root) {
    // init SVG
    const svgContainer = document.getElementById('svg-container');
    while (svgContainer.firstChild) {
        svgContainer.removeChild(svgContainer.firstChild);
    }

    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("width", "10000");
    svg.setAttribute("height", "10000");
    svgContainer.appendChild(svg);
    
    // if input root
    if (root === "") {
        const virtualRoot = {
            name: "root",
            kid: findRoots(),
            url: "#"
        };

        dag[virtualRoot.name] = virtualRoot;
        root = "root";
    }

    // Graph
    position = bfs(root);

    let elements_num = Array(100).fill(0);
    for (let key in position) {
        let value = position[key];
        elements_num[value[0]] = Math.max(elements_num[value[0]], value[1] + 1);
    }

    let elements_num_max = Math.max(...elements_num);
    for (let key in position) {
        let value = position[key];
        value[1] = (elements_num_max * 50) / elements_num[value[0]] * (value[1] + 0.5);
        value[0] = (value[0] + 1) * 300 - 200;
    }

    draw(svg, dag[root], position, new Set());

    if(root === "root") {
        delete dag[root];
    }
}

function findRoots() {
    const allNodes = new Set(Object.keys(dag));
    for (let nodeName in dag) {
        for (let kid of dag[nodeName].kid) {
            allNodes.delete(kid);
        }
    }
    return Array.from(allNodes);
}

function bfs(root) {
    const position = {};
    const queue = [dag[root]];
    let level = -1;

    while (queue.length) {
        const n = queue.length;
        level += 1;
        for (let i = 0; i < n; i++) {
            const node = queue.shift();
            position[node.name] = [level, i];
            node.kid.forEach(kidName => {
                const kid = dag[kidName];
                if (!(kidName in position)) {
                    queue.push(kid);
                    position[kidName] = [-1, -1];
                }
            });
        }
    }

    return position;
}

function draw(svg, node, position, visited) {
    const radius = 8;
    
    node.kid.forEach(kidName => {
        const child = dag[kidName];

        drawEdge(svg, 
            position[node.name][0] + radius, 
            position[node.name][1], 
            position[child.name][0] - radius, 
            position[child.name][1]);

        if (!visited.has(kidName)) {
            visited.add(kidName);
            draw(svg, child, position, visited);
        }
    });

    [x, y] = position[node.name];
    drawNode(svg, x, y, node.name, node.url);
}

function drawNode(svg, x, y, node_name, node_url) {
    const radius = 8;
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", x);
    circle.setAttribute("cy", y);
    circle.setAttribute("r", radius);
    circle.setAttribute("stroke", "red");
    circle.setAttribute("fill", "#FF8888");
    circle.setAttribute("stroke-width", "2");

    const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
    text.setAttribute("x", x + radius * 1.5);
    text.setAttribute("y", y + radius / 1.25);
    text.setAttribute("font-family", "Times New Roman");
    text.setAttribute("font-size", "20");
    text.textContent = node_name;

    const circleLink = document.createElementNS("http://www.w3.org/2000/svg", "a");
    circleLink.setAttribute("href", "javascript:void(0)");  // You can use this to prevent default link action
    circleLink.addEventListener('click', () => drawDAG(node_name));

    const textLink = document.createElementNS("http://www.w3.org/2000/svg", "a");
    textLink.setAttribute("href", node_url);

    circleLink.appendChild(circle);
    textLink.appendChild(text);
    svg.appendChild(circleLink);
    svg.appendChild(textLink);
}

function drawEdge(svg, x1, y1, x2, y2) {
    const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
    const d = `M ${x1} ${y1} C ${(x1 + x2) / 2} ${y1} ${(x1 + x2) / 2} ${y2} ${x2} ${y2}`;

    path.setAttribute("d", d);
    path.setAttribute("stroke", "#8888FF");
    path.setAttribute("fill", "none");
    path.setAttribute("stroke-width", "1");
    svg.appendChild(path);
}


