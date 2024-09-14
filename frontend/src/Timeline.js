// src/Timeline.js
import React, { useEffect, useState, useRef } from 'react';
import './styles/Timeline.css';

const Timeline = ({ lineLength = 1600, lineWidth = 600, amplitude = 200, frequency = 200 }) => {
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
      const rect = timelineSection.getBoundingClientRect();
      const viewportHeight = window.innerHeight;
      
      // Calculate how much of the section is above the viewport
      const sectionAbove = Math.max(0, -rect.top);
      
      // Calculate the scroll progress
      const scrollProgress = sectionAbove / (rect.height - viewportHeight);
      
      // Ensure the scroll progress is between 0 and 1
      const scrolled = Math.max(0, Math.min(1, scrollProgress));
      
      setScrollPercent(scrolled);
    };

    window.addEventListener('scroll', handleScroll);
    // Initial call to set the correct position on load
    handleScroll();

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
          height={lineLength}
        >
          {/* Barely visible path */}
          <path d={pathData} className="timeline-dark-path" />

          {/* Brighter path that reveals on scroll */}
          <path
            ref={pathRef}
            d={pathData}
            className="timeline-bright-line" 
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
