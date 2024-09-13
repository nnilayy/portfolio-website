// src/Timeline.js
import React, { useEffect, useState, useRef } from 'react';
import './Timeline.css';

const Timeline = ({ lineLength = 1600, lineWidth = 400, amplitude = 150, frequency = 400 }) => {
  const [scrollPercent, setScrollPercent] = useState(0);
  const timelineSectionRef = useRef(null);
  const pathRef = useRef(null);
  const [totalLength, setTotalLength] = useState(0);

  useEffect(() => {
    const pathElement = pathRef.current;
    const length = pathElement.getTotalLength();
    setTotalLength(length);

    const timelineSection = timelineSectionRef.current;

    const handleScroll = () => {
      const scrollTop = window.scrollY;
      const offsetTop = timelineSection.offsetTop;
      const sectionHeight =
        timelineSection.offsetHeight - window.innerHeight;
      const scrolled = Math.min(
        Math.max((scrollTop - offsetTop) / sectionHeight, 0),
        1
      );
      setScrollPercent(scrolled);
    };

    window.addEventListener('scroll', handleScroll);

    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  // Generate path data dynamically, ensuring the line is centered horizontally
  const generatePathData = (amplitude, frequency, totalHeight) => {
    let pathData = `M ${lineWidth / 2} 0`; // Start in the center of the width

    for (let y = 0; y < totalHeight; y += frequency) {
      const controlPoint1X = lineWidth / 2 + amplitude; // Shift right from center
      const controlPoint2X = lineWidth / 2 - amplitude; // Shift left from center
      const endY = y + frequency;

      pathData += ` C ${controlPoint1X} ${y + frequency / 2}, ${controlPoint2X} ${y + frequency / 2}, ${lineWidth / 2} ${endY}`;
    }

    return pathData;
  };

  const pathData = generatePathData(amplitude, frequency, lineLength);

  return (
    <section
      id="timeline-section"
      className="timeline-section"
      ref={timelineSectionRef}
    >
      <div className="timeline-container">
        <svg
          viewBox={`0 0 ${lineWidth} ${lineLength}`} /* Dynamic viewBox */
          preserveAspectRatio="xMidYMin meet"
          className="timeline-svg"
          width="100%"
          height={lineLength}
        >
          {/* Barely visible path */}
          <path d={pathData} stroke="#ccc" strokeWidth="4" fill="none" />

          {/* Brighter path that reveals on scroll */}
          <path
            ref={pathRef}
            d={pathData}
            stroke="#007bff"
            strokeWidth="4"
            fill="none"
            strokeDasharray={totalLength}
            strokeDashoffset={
              totalLength - scrollPercent * totalLength
            }
          />
        </svg>
      </div>
    </section>
  );
};

export default Timeline;
