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
  }, [handleScroll]);

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
          <path d={generatePathData} className="timeline-dark-path" />
          {/* Bright Path */}
          <path
            ref={pathRef}
            d={generatePathData}
            className="timeline-bright-line"
            strokeDasharray={totalLength}
            strokeDashoffset={totalLength - scrollPercent * totalLength}
          />
          {/* Checkpoints */}
          <Checkpoints
            numCheckpoints={numCheckpoints}
            data={data}
            pathData={generatePathData}
            scrollPercent={scrollPercent}
          />
        </svg>
      </div>
    </section>
  );
};

export default Timeline;
