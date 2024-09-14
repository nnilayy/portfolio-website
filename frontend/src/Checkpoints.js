import React, { useMemo } from 'react';
import './styles/Checkpoints.css';
import RectanglePopup from './RectanglePopup';

const calculatePathBounds = (pathData) => {
  const tempPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
  tempPath.setAttribute('d', pathData);
  const totalPathLength = tempPath.getTotalLength();

  let minX = Infinity;
  let maxX = -Infinity;

  for (let i = 0; i <= totalPathLength; i += 100) {
    const point = tempPath.getPointAtLength(i);
    minX = Math.min(minX, point.x);
    maxX = Math.max(maxX, point.x);
  }

  return { minX, maxX, totalPathLength, tempPath };
};

const Checkpoints = ({ numCheckpoints, pathData, scrollPercent }) => {
  const { checkpoints, pathBounds } = useMemo(() => {
    const totalCheckpoints = numCheckpoints + 2;
    const { minX, maxX, totalPathLength, tempPath } = calculatePathBounds(pathData);

    const checkpoints = Array.from({ length: totalCheckpoints }, (_, i) => {
      const position = i / (totalCheckpoints - 1);
      const lengthAtPoint = position * totalPathLength;
      const { x, y } = tempPath.getPointAtLength(lengthAtPoint);

      return {
        x,
        y,
        isMiddleCheckpoint: i > 0 && i < totalCheckpoints - 1,
        popupDirection: i % 2 === 0 ? 'left' : 'right',
        index: i,
        position
      };
    });

    return { checkpoints, pathBounds: { minX, maxX } };
  }, [numCheckpoints, pathData]);

  return (
    <>
      {checkpoints.map(({ x, y, isMiddleCheckpoint, popupDirection, index, position }) => {
        const isPassed = scrollPercent >= position;
        return (
          <g key={index}>
            <circle
              cx={x}
              cy={y}
              r={10}
              className={`checkpoint ${isPassed ? 'passed' : ''}`}
            />
            {isMiddleCheckpoint && (
              <RectanglePopup
                x={x}
                y={y}
                direction={popupDirection}
                content={`Checkpoint ${index}`}
                isVisible={isPassed}
                pathBounds={pathBounds}
              />
            )}
          </g>
        );
      })}
    </>
  );
};

export default React.memo(Checkpoints);
