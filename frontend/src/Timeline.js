// Timeline.js
import React, { useEffect, useState, useRef, useMemo, useCallback } from 'react';
import './styles/Timeline.css';
import Checkpoints from './Checkpoints';

const Timeline = ({
  lineLength = 1600,
  lineWidth = 600,
  amplitude = 200,
  frequency = 400,
  numCheckpoints = 0,
  data = [],
  colors = {},
  speed = 1, // Default speed multiplier
}) => {
  const [scrollPercent, setScrollPercent] = useState(0);
  const timelineSectionRef = useRef(null);
  const pathRef = useRef(null);
  const [totalLength, setTotalLength] = useState(0);

  const generatePathData = useMemo(() => {
    const halfLineWidth = lineWidth / 2;
    let pathData = `M ${halfLineWidth} 0`;
    for (let y = 0; y < lineLength; y += frequency) {
      const controlPoint1X = halfLineWidth + amplitude;
      const controlPoint2X = halfLineWidth - amplitude;
      const endY = y + frequency;
      const midY = y + frequency / 2;
      pathData += ` C ${controlPoint1X} ${midY}, ${controlPoint2X} ${midY}, ${halfLineWidth} ${endY}`;
    }
    return pathData;
  }, [lineWidth, lineLength, amplitude, frequency]);

  const handleScroll = useCallback(() => {
    const timelineSection = timelineSectionRef.current;
    if (!timelineSection) return;

    const rect = timelineSection.getBoundingClientRect();
    const viewportHeight = window.innerHeight;
    const sectionAbove = Math.max(0, -rect.top);
    const scrollProgress = sectionAbove / (rect.height - viewportHeight);
    const scrolled = Math.max(0, Math.min(1, scrollProgress));
    setScrollPercent(scrolled);
  }, []);

  useEffect(() => {
    const pathElement = pathRef.current;
    if (pathElement) {
      const length = pathElement.getTotalLength();
      setTotalLength(length);
    }

    window.addEventListener('scroll', handleScroll);
    handleScroll();

    return () => window.removeEventListener('scroll', handleScroll);
    // Include dependencies that affect the path
  }, [handleScroll, lineLength, lineWidth, amplitude, frequency]);

  // Adjust scroll percent with speed multiplier
  const adjustedScrollPercent = Math.min(1, scrollPercent * speed);

  return (
    <section className="timeline-section" ref={timelineSectionRef}>
      <div className="timeline-container">
        <svg
          viewBox={`0 -15 ${lineWidth} ${lineLength + 35}`}
          preserveAspectRatio="xMidYMin meet"
          className="timeline-svg"
          height={lineLength}
        >
          {/* Dark Path */}
          <path
            d={generatePathData}
            stroke={colors.timelineDarkPath || '#212120'}
            strokeWidth={5}
            fill="none"
          />
          {/* Bright Path */}
          <path
            ref={pathRef}
            d={generatePathData}
            stroke="#fff"
            strokeWidth={5}
            fill="none"
            strokeDasharray={totalLength}
            strokeDashoffset={totalLength - adjustedScrollPercent * totalLength}
            style={{ filter: `drop-shadow(0 0 6px ${colors.timelineBrightLine || '#ff3030'})` }}
          />
          {/* Checkpoints */}
          <Checkpoints
            numCheckpoints={numCheckpoints}
            data={data}
            pathData={generatePathData}
            scrollPercent={adjustedScrollPercent} // Use adjusted scroll percent
            colors={colors}
          />
        </svg>
      </div>
    </section>
  );
};
export default Timeline;