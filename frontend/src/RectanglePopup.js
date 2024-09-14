import React from 'react';
import './styles/RectanglePopup.css';

const RectanglePopup = ({ x, y, direction, content, isVisible, pathBounds }) => {
  const popupWidth = 220;
  const popupHeight = 200;
  const margin = 20;

  const popupX = direction === 'left'
    ? pathBounds.minX - popupWidth - margin
    : pathBounds.maxX + margin;

  const popupY = y - popupHeight / 2 + 80;

  return (
    <g className={`rectangle-popup ${direction} ${isVisible ? 'visible' : ''}`}>
      <rect
        x={popupX}
        y={popupY}
        width={popupWidth}
        height={popupHeight}
        rx={10}
        ry={10}
      />
      <text
        x={popupX + popupWidth / 2}
        y={popupY + popupHeight / 2}
        textAnchor="middle"
        dominantBaseline="middle"
      >
        {content}
      </text>
    </g>
  );
};

const areEqual = (prevProps, nextProps) => 
  prevProps.isVisible === nextProps.isVisible && prevProps.content === nextProps.content;

export default React.memo(RectanglePopup, areEqual);
