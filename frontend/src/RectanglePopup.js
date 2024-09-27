// RectanglePopup.js

import React, { useState, useEffect } from 'react';
import './styles/RectanglePopup.css';
import { CSSTransition, TransitionGroup } from 'react-transition-group';

const RectanglePopup = ({ x, y, direction, content, isVisible, pathBounds }) => {
  const popupWidth = 220;
  const popupHeight = 200;
  const margin = 20;

  const popupX =
    direction === 'left'
      ? pathBounds.minX - popupWidth - margin
      : pathBounds.maxX + margin;

  const popupY = y - popupHeight / 2 + 80;

  // Initialize currentPage state
  const [currentPage, setCurrentPage] = useState(0);

  // Reset currentPage when content changes or when popup becomes visible
  useEffect(() => {
    if (isVisible) {
      setCurrentPage(0);
    }
  }, [content, isVisible]);

  // Ensure content is an array
  const contentArray = content || [];
  const totalPages = contentArray.length;

  const handlePrev = () => {
    setCurrentPage((prevPage) => (prevPage - 1 + totalPages) % totalPages);
  };

  const handleNext = () => {
    setCurrentPage((prevPage) => (prevPage + 1) % totalPages);
  };

  return (
    <g
      className={`rectangle-popup ${direction} ${
        isVisible ? 'visible' : ''
      }`}
    >
      <foreignObject
        x={popupX}
        y={popupY}
        width={popupWidth}
        height={popupHeight}
      >
        <div
          xmlns="http://www.w3.org/1999/xhtml"
          className="popup-container"
        >
          <div className="popup-header">
            <button className="left-button" onClick={handlePrev}>
              &lt;
            </button>
            {/* Replace page indicator text with circles */}
            <div className="page-indicator">
              {Array.from({ length: totalPages }).map((_, index) => (
                <div
                  key={index}
                  className={`indicator-dot ${
                    index === currentPage ? 'active' : ''
                  }`}
                ></div>
              ))}
            </div>
            <button className="right-button" onClick={handleNext}>
              &gt;
            </button>
          </div>

          {/* Add TransitionGroup and CSSTransition for animating content */}
          <div className="popup-content">
            <TransitionGroup>
              <CSSTransition
                key={currentPage}
                timeout={300}
                classNames="fade"
              >
                <div className="content-page">
                  {contentArray[currentPage]}
                </div>
              </CSSTransition>
            </TransitionGroup>
          </div>
          {/* End of TransitionGroup and CSSTransition */}
        </div>
      </foreignObject>
    </g>
  );
};

const areEqual = (prevProps, nextProps) =>
  prevProps.isVisible === nextProps.isVisible &&
  prevProps.content === nextProps.content;

export default React.memo(RectanglePopup, areEqual);
