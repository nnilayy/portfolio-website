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
  const [loading, setLoading] = useState(true);
  const [loadingSection, setLoadingSection] = useState(false);

  useEffect(() => {
    // Fetch sections, sectionColors, and sectionData from the backend
    const fetchData = async () => {
      try {
        const [sectionsRes, colorsRes, dataRes] = await Promise.all([
          axios.get('http://127.0.0.1:8000/sections'),
          axios.get('http://127.0.0.1:8000/section_colors'),
          axios.get('http://127.0.0.1:8000/section_data'),
        ]);
        setSections(sectionsRes.data);
        setSectionColors(colorsRes.data);
        setSectionData(dataRes.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching data from backend:', error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const handleSectionClick = (section) => {
    // Toggle selected section
    setSelectedSection((prevSection) => (prevSection === section ? null : section));
  };

  // if (loading) {
  //   return <div>Loading...</div>; // Or any loading indicator
  // }

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
      {selectedSection && sectionData[selectedSection] && sectionColors[selectedSection] ? (
        <Timeline
          numCheckpoints={sectionData[selectedSection].numCheckpoints}
          data={sectionData[selectedSection].data}
          colors={sectionColors[selectedSection]}
        />
      ) : (
        selectedSection && <div>No data available for this section.</div>
      )}
    </div>
  );
};

export default WorkSections;
