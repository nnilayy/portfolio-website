// Checkpoints.js
import React, { useMemo } from 'react';
import './styles/Checkpoints.css';
import RectanglePopup from './RectanglePopup';

const calculatePathBounds = (pathData) => {
  const tempPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
  tempPath.setAttribute('d', pathData);
  const totalPathLength = tempPath.getTotalLength();

  let minX = Infinity;
  let maxX = -Infinity;

  for (let i = 0; i <= totalPathLength; i += 10) {
    const point = tempPath.getPointAtLength(i);
    minX = Math.min(minX, point.x);
    maxX = Math.max(maxX, point.x);
  }

  return { minX, maxX, totalPathLength, tempPath };
};

const Checkpoints = ({ numCheckpoints, data, pathData, scrollPercent, colors }) => {
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
        position,
        data: data[i - 1] || {}, // Adjust index since we have extra checkpoints
      };
    });

    return { checkpoints, pathBounds: { minX, maxX } };
  }, [numCheckpoints, data, pathData]);

  return (
    <>
      {checkpoints.map(({ x, y, isMiddleCheckpoint, popupDirection, index, position, data }) => {
        const isPassed = scrollPercent >= position;
        return (
          <g key={index}>
            <circle
              cx={x}
              cy={y}
              r={10}
              style={{
                fill: isPassed ? colors.checkpointPassedColor : colors.checkpointDefaultColor,
                filter: isPassed ? `drop-shadow(0 0 6px ${colors.checkpointGlowColor})` : 'none',
                transition: 'fill 0.5s ease, filter 0.5s ease',
              }}
            />
            {isMiddleCheckpoint && data.content && (
              <RectanglePopup
                x={x}
                y={y}
                direction={popupDirection}
                content={data.content}
                isVisible={isPassed}
                pathBounds={pathBounds}
                colors={colors} // Pass colors to RectanglePopup
              />
            )}
          </g>
        );
      })}
    </>
  );
};

export default React.memo(Checkpoints);
