// https://adventofcode.com/2019/day/3
const wirePath1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',');
const wirePath2 = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',');

const segmentReader = (segment) => {
    const direction = segment.slice(0,1);
    const distance = +segment.slice(1);
    switch(direction) {
        case 'R': return { x: distance };
        case 'L': return  { x: -distance };
        case 'U': return { y: distance };
        case 'D': return { y: -distance };
        default: console.log('ERROR');
    }
};

const segmentTracer = (rawSegment, position={x: 0, y: 0}) => {
    const segment = segmentReader(rawSegment);
    let segmentPositions = [];
    for (let point = 1; point <= Math.abs(segment.x); point++)
        segmentPositions.push({ x: position.x + Math.sign(segment.x) * point, y: position.y });
    for (let point = 1; point <= Math.abs(segment.y); point++)
        segmentPositions.push({ x: position.x, y: position.y + Math.sign(segment.y) * point });
    return segmentPositions;
};

const pathTracer = (path) => path.reduce((seq, segment) => [...seq, ...segmentTracer(segment, seq.slice(-1)[0])], []);

const wireIntersections = (wire1, wire2) => {
    const path1 = pathTracer(wire1).map(point => JSON.stringify(point));
    const path2 = pathTracer(wire2).map(point => JSON.stringify(point));
    let intersections = [];
    path1.forEach((point, requiredSteps1) => {
        const requiredSteps2 = path2.indexOf(point);
        if (requiredSteps2 > -1)
            intersections.push({ intersection: JSON.parse(point), steps: requiredSteps1 + requiredSteps2 + 2 });
    });
    return intersections;
};

const awnsers = (intersections) => ({
    1: Math.min(...intersections.map(({intersection: i}) => Math.abs(i.x) + Math.abs(i.y))),
    2: Math.min(...intersections.map(({ steps }) => steps)),
});

console.log(awnsers(wireIntersections(wirePath1, wirePath2)));