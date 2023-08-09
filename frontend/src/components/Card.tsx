import React, { useState, useEffect } from "react"
import "./Card.css"

interface CardProps {
    apiUrl: string;
}

const Card: React.FC = () => {
  return (
    <>
    <div className="card-container">
      <img src="" alt="Card Image" className="card-img" />
      <h1 className="card-title">Card Title</h1>
      <p className="card-description">Description</p>
      <a href="cardPage" className="card-btn">
        Learn More
      </a>
    </div>
    </>
  )
};

export default Card;
