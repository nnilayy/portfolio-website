// WorkSections.js

import React, { useState, useEffect } from 'react';
import Timeline from './Timeline';
import './styles/WorkSections.css';
import axios from 'axios';

const WorkSections = () => {
  const [selectedSection, setSelectedSection] = useState(null);
  const [sections, setSections] = useState([]);
  const [sectionColors, setSectionColors] = useState({});
  const [sectionData, setSectionData] = useState({});
  const [sectionTimelineProps, setSectionTimelineProps] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch sections, sectionColors, sectionData, and sectionTimelineProps from the backend
    const fetchData = async () => {
      try {
        const [sectionsRes, colorsRes, dataRes, timelinePropsRes] = await Promise.all([
          axios.get('http://127.0.0.1:8000/sections'),
          axios.get('http://127.0.0.1:8000/section_colors'),
          axios.get('http://127.0.0.1:8000/section_data'),
          axios.get('http://127.0.0.1:8000/section_timeline_properties'),
        ]);
        setSections(sectionsRes.data);
        setSectionColors(colorsRes.data);
        setSectionData(dataRes.data);
        setSectionTimelineProps(timelinePropsRes.data);
        setLoading(false);

        // Set the default selected section to the first one
        if (sectionsRes.data.length > 0) {
          setSelectedSection(sectionsRes.data[0]);
        }
      } catch (error) {
        console.error('Error fetching data from backend:', error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const handleSectionClick = (section) => {
    // Always set the selected section to the clicked one
    setSelectedSection(section);
  };

  return (
    <div id="work" className="work-sections">
      {/* Section Buttons */}
      <div className="section-buttons">
        {sections.map((section) => (
          <button
            key={section}
            className={`work-section-button ${selectedSection === section ? 'active' : ''}`}
            onClick={() => handleSectionClick(section)}
          >
            {section}
          </button>
        ))}
      </div>

      {/* Timeline for Selected Section */}
      {selectedSection &&
      sectionData[selectedSection] &&
      sectionColors[selectedSection] &&
      sectionTimelineProps[selectedSection] ? (
        <Timeline
          lineLength={sectionTimelineProps[selectedSection].lineLength}
          lineWidth={sectionTimelineProps[selectedSection].lineWidth}
          amplitude={sectionTimelineProps[selectedSection].amplitude}
          frequency={sectionTimelineProps[selectedSection].frequency}
          speed={sectionTimelineProps[selectedSection].speed} // Pass speed prop
          numCheckpoints={sectionData[selectedSection].numCheckpoints}
          data={sectionData[selectedSection].checkpoints}
          colors={sectionColors[selectedSection]}
        />
      ) : (
        <div></div>
      )}
    </div>
  );
};

export default WorkSections;