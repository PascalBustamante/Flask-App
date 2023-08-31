import React, { useState, useEffect } from "react"
import "./Card.css"

interface CardProps {

}

const Card: React.FC = ({data}:any) => {
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
