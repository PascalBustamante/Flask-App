import React from "react"

interface ButtonProps {
    children: string;
    color?: 'primary' | 'secondary' | 'danger';
    onClick: () => void; 
}

const handleClick = () => {
    console.log('pressed!!')
}

const Button = ({ children, onClick, color = 'primary' }: ButtonProps) => {
    return(
        <button className={'btn btn-' + color} onClick={onClick}>{children}</button> 
    );
}

export default Button;