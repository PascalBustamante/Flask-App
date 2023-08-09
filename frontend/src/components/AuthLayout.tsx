import React, { useState, useEffect } from "react"
import Card from "./Card"
import "./AuthLayout.css"

interface CardProps {
    apiUrl: string;
}

const AuthLayout: React.FC = () => {
    return (
      <>
      <div className="auth-layout">
        <Card />
      </div>
      </>
    )
  };
  
  export default AuthLayout;