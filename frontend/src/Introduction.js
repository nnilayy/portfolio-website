// src/Introduction.js
import React, { useEffect, useRef } from 'react';
import './styles/Introduction.css';
import { BlobContainer } from './Blob';

const Introduction = () => {
  const introRef = useRef(null);

  useEffect(() => {
    const currentRef = introRef.current;
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      },
      { threshold: 0.1 }
    );

    if (currentRef) {
      observer.observe(currentRef);
    }

    return () => {
      if (currentRef) {
        observer.unobserve(currentRef);
      }
    };
  }, []);

  return (
    <section className="introduction" ref={introRef}>
      <BlobContainer />
      <div className="content">
        <h1>Hello, I'm [Your Name]</h1>
        <p>
          [Write a brief introduction about yourself here. You can talk about your journey into machine learning, your interests, and any other details you'd like to share.]
        </p>
      </div>
    </section>
  );
};

export default Introduction;
