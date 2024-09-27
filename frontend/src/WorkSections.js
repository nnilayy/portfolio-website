// WorkSections.js
import React, { useState } from 'react';
import Timeline from './Timeline';
import './styles/WorkSections.css';

const WorkSections = () => {
  const [selectedSection, setSelectedSection] = useState(null);

  const sections = ['Blogs', 'Research', 'Internships', 'Projects', 'Extensions'];

  // Define data for each section with multiple pages per checkpoint
  const sectionData = {
    Blogs: {
      numCheckpoints: 3,
      data: [
        { content: ['Blog Post 1 - Page 1', 'Blog Post 1 - Page 2'] },
        { content: ['Blog Post 2 - Only Page'] },
        { content: ['Blog Post 3 - Page 1', 'Blog Post 3 - Page 2', 'Blog Post 3 - Page 3'] },
      ],
    },
    Research: {
      numCheckpoints: 4,
      data: [
        { content: ['Research Paper 1 - Page 1', 'Research Paper 1 - Page 2'] },
        { content: ['Research Paper 2 - Only Page'] },
        { content: ['Research Paper 3 - Page 1', 'Research Paper 3 - Page 2'] },
        { content: ['Research Paper 4 - Page 1', 'Research Paper 4 - Page 2', 'Research Paper 4 - Page 3'] },
      ],
    },
    Internships: {
      numCheckpoints: 5,
      data: [
        { content: ['Internship 1 - Page 1'] },
        { content: ['Internship 2 - Page 1', 'Internship 2 - Page 2'] },
        { content: ['Internship 3 - Only Page'] },
        { content: ['Internship 4 - Page 1', 'Internship 4 - Page 2', 'Internship 4 - Page 3'] },
        { content: ['Internship 5 - Page 1', 'Internship 5 - Page 2'] },
      ],
    },
    Projects: {
      numCheckpoints: 6,
      data: [
        { content: ['Project 1 - Only Page'] },
        { content: ['Project 2 - Page 1', 'Project 2 - Page 2'] },
        { content: ['Project 3 - Page 1', 'Project 3 - Page 2', 'Project 3 - Page 3'] },
        { content: ['Project 4 - Only Page'] },
        { content: ['Project 5 - Page 1', 'Project 5 - Page 2'] },
        { content: ['Project 6 - Page 1', 'Project 6 - Page 2'] },
      ],
    },
    Extensions: {
      numCheckpoints: 2,
      data: [
        { content: ['Extension 1 - Only Page'] },
        { content: ['Extension 2 - Page 1', 'Extension 2 - Page 2'] },
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
        <Timeline
          numCheckpoints={sectionData[selectedSection].numCheckpoints}
          data={sectionData[selectedSection].data}
        />
      )}
    </div>
  );
};

export default WorkSections;
