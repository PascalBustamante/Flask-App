import { error } from "console";
import React, { useContext, useState } from "react";
import { Context } from "vm";

export const Login = () => {
    const {store, actions} = useContext(Context);
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleClick = () => {

        const opts = {
            method: 'POST',
            body: JSON.stringify({
                'email': email,
                'password': password
            })
        }

        fetch("/login", opts)
            .then(resp => {
                if (resp.status == 200) return resp.json();
                else alert("there was an error!", error);
            })
            .then()
    }

    <div className="text-center">
        <h1>Login</h1>
        <div>
            <input type="text" placeholder="email" value={email} onChange={(e) => setEmail(e.target.value)} />
            <input type="text" placeholder="password" value={password} onChange={(e) => setPassword(e.target.value)} />
            <button> Login</button>
        </div>
    </div>
}