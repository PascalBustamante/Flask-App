import React, { useEffect, useState, useRef } from "react";
import './login.css';
import useSubmit from "../utils/useSubmit";

const Login = () => {
    const { response, error, isLoading, performSubmit } = useSubmit();

    const errRef = useRef<HTMLInputElement | null>(null); 

    const [username, setUsername] = useState('');
    const [usernameFocus, setUsernameFocus] = useState(false);

    const [pwd, setPwd] = useState('');
    const [pwdFocus, setPwdFocus] = useState(false);

    const [errMsg, setErrMsg] = useState('');
    const [success, setSuccess] = useState(Boolean);

    const handleSubmit =async (e: React.FormEvent): Promise<void> => {
        e.preventDefault;
        const formData = {
            'username': username,
            'password': pwd
        };
        await performSubmit('http://127.0.0.1:5000/auth/login', 'POST', formData);
        console.log(formData);
    }

    return (
        <>
        {success ? (
            <section>
                <h1>Success!</h1>
                <p>
                    <a href="#">Profile</a>
                </p>
            </section>
        ) : (
        <section>
            <p ref={errRef} className={errMsg ? 'errmsg' : 'offscreen'} aria-live="assertive">{errMsg}</p>
            <h1>Login</h1>
            <form>
                <label htmlFor="username">
                    username:
                </label>
                <input  
                    type="text"
                    id="username"
                    autoComplete="off"
                    onChange={(e) => setUsername(e.target.value)}
                    required
                    onFocus={() => setUsernameFocus(true)}
                    onBlur={() => setUsernameFocus(false)}
                    />

                <label htmlFor="password">
                    Password:
                </label>
                <input  
                    type="password"
                    id="password"
                    onChange={(e) => setPwd(e.target.value)}
                    required
                    onFocus={() => setPwdFocus(true)}
                    onBlur={() => setPwdFocus(false)}
                    />
                    
                    <button type='button' onClick={handleSubmit} disabled={!username || !pwd || isLoading ? true : false}>Login</button>
            </form>
            <p>
                Not registered?<br />
                <span className="line">
                    {/*put router link here*/}
                    <a href="#">Register</a>
                </span>
            </p>
        </section>
        )
        }
        </>
    )
}

export default Register;
