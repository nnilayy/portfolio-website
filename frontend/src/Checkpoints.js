// src/Checkpoints.js
import React, { useEffect, useState } from 'react';
import './styles/Checkpoints.css';

const Checkpoints = ({ numCheckpoints, lineLength, pathData, scrollPercent }) => {
  const [checkpoints, setCheckpoints] = useState([]);

  useEffect(() => {
    const totalCheckpoints = numCheckpoints + 2; // Including start and end
    const tempCheckpoints = [];

    // Create a temporary SVG path element
    const tempPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    tempPath.setAttribute('d', pathData);
    const totalPathLength = tempPath.getTotalLength();

    for (let i = 0; i < totalCheckpoints; i++) {
      const position = i / (totalCheckpoints - 1);
      const lengthAtPoint = position * totalPathLength;
      const point = tempPath.getPointAtLength(lengthAtPoint);

      const isPassed = scrollPercent >= position;

      tempCheckpoints.push(
        <circle
          key={i}
          cx={point.x}
          cy={point.y}
          r={10}
          className={`checkpoint ${isPassed ? 'passed' : ''}`}
        />
      );
    }

    setCheckpoints(tempCheckpoints);
  }, [numCheckpoints, lineLength, pathData, scrollPercent]);

  return <>{checkpoints}</>;
};

export default Checkpoints;
