// RectanglePopup.js

import React, { useState, useEffect, useRef } from 'react';
import './styles/RectanglePopup.css';
import './styles/RectanglePopUpPageLayouts/DefaultLayout.css'
import { CSSTransition, TransitionGroup } from 'react-transition-group';

const RectanglePopup = ({ x, y, direction, content, isVisible, pathBounds, colors }) => {
  const popupWidth = 220;
  const popupHeight = 200;
  const margin = 20;

  const popupX =
    direction === 'left'
      ? pathBounds.minX - popupWidth - margin
      : pathBounds.maxX + margin;

  const popupY = y - popupHeight / 2 + 80;

  // Page state for navigation
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

  // Refs for swipe detection
  const startXRef = useRef(0);
  const deltaXRef = useRef(0);

  // Touch event handlers for swipe detection
  const handleTouchStart = (e) => {
    startXRef.current = e.touches[0].clientX;
    deltaXRef.current = 0;
  };

  const handleTouchMove = (e) => {
    deltaXRef.current = e.touches[0].clientX - startXRef.current;
  };

  const handleTouchEnd = () => {
    const deltaX = deltaXRef.current;
    const threshold = 50; // Minimum swipe distance in pixels

    if (deltaX > threshold) {
      // Swiped right
      handlePrev();
    } else if (deltaX < -threshold) {
      // Swiped left
      handleNext();
    }

    // Reset deltaXRef
    deltaXRef.current = 0;
  };

  return (
    <g
      className={`rectangle-popup ${direction} ${isVisible ? 'visible' : ''}`}
    >
      <foreignObject
        x={popupX}
        y={popupY}
        width={popupWidth}
        height={popupHeight}
        className="popup-foreign-object"
        style={{ boxShadow: colors.boxShadow }}
      >
        <div
          xmlns="http://www.w3.org/1999/xhtml"
          className="popup-container"
          onTouchStart={handleTouchStart}
          onTouchMove={handleTouchMove}
          onTouchEnd={handleTouchEnd}
        >
          <div className="popup-header">
            <button className="left-button" onClick={handlePrev}>
              &lt;
            </button>
            <div className="page-indicator">
              {Array.from({ length: totalPages }).map((_, index) => (
                <div
                  key={index}
                  className={`indicator-dot ${index === currentPage ? 'active' : ''}`}
                ></div>
              ))}
            </div>
            <button className="right-button" onClick={handleNext}>
              &gt;
            </button>
          </div>
          <div className="popup-content">
            <TransitionGroup>
              <CSSTransition
                key={currentPage}
                timeout={300}
                classNames="fade"
              >
                <div className="content-page">
                  {/* Title */}
                  {contentArray[currentPage]?.title && (
                    <p className='content-page-title'><i>{contentArray[currentPage].title}</i></p>
                  )}

                  <div className='content'>
                    {/* Content*/}
                    {contentArray[currentPage]?.content && (
                      <p className='content-page-content'>{contentArray[currentPage].content}</p>
                    )}

                    {/* Image */}
                    {contentArray[currentPage]?.image && (
                      <p className='content-page-image'>{contentArray[currentPage].image}</p>
                    )}

                    {/* Video */}
                    {contentArray[currentPage]?.video && (
                      <p className='content-page-video'>{contentArray[currentPage].video}</p>
                    )}

                    {/* Link */}
                    {contentArray[currentPage]?.link && (
                      <p className='content-page-link'>{contentArray[currentPage].link}</p>
                    )}
                  </div>

                </div>
              </CSSTransition>
            </TransitionGroup>
          </div>
        </div>
      </foreignObject>
    </g>
  );
};

const areEqual = (prevProps, nextProps) =>
  prevProps.isVisible === nextProps.isVisible &&
  prevProps.content === nextProps.content;

export default React.memo(RectanglePopup, areEqual);
