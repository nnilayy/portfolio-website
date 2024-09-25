// WorkSections.js
import React, { useState } from 'react';
import Timeline from './Timeline';
import './styles/WorkSections.css';

const WorkSections = () => {
  const [selectedSection, setSelectedSection] = useState(null);

  const sections = ['Blogs', 'Research', 'Internships', 'Projects', 'Extensions'];

  // Define data for each section
  const sectionData = {
    Blogs: {
      numCheckpoints: 3,
      data: [
        { content: 'Blog Post 1' },
        { content: 'Blog Post 2' },
        { content: 'Blog Post 3' },
      ],
    },
    Research: {
      numCheckpoints: 4,
      data: [
        { content: 'Research Paper 1' },
        { content: 'Research Paper 2' },
        { content: 'Research Paper 3' },
        { content: 'Research Paper 4' },
      ],
    },
    Internships: {
      numCheckpoints: 5,
      data: [
        { content: 'Internship 1' },
        { content: 'Internship 2' },
        { content: 'Internship 3' },
        { content: 'Internship 4' },
        { content: 'Internship 5' },
      ],
    },
    Projects: {
      numCheckpoints: 6,
      data: [
        { content: 'Project 1' },
        { content: 'Project 2' },
        { content: 'Project 3' },
        { content: 'Project 4' },
        { content: 'Project 5' },
        { content: 'Project 6' },
      ],
    },
    Extensions: {
      numCheckpoints: 2,
      data: [
        { content: 'Extension 1' },
        { content: 'Extension 2' },
      ],
    },
  };

  const handleSectionClick = (section) => {
    // Set the selected section; if the same section is clicked, deselect it
    setSelectedSection((prevSection) => (prevSection === section ? null : section));
  };

  return (
    <div className="work-sections">
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
      {selectedSection && (
        <div className="timeline-wrapper">
          <Timeline
            numCheckpoints={sectionData[selectedSection].numCheckpoints}
            data={sectionData[selectedSection].data}
          />
        </div>
      )}
    </div>
  );
};

export default WorkSections;
