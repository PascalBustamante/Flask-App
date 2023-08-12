import React, { useEffect, useState, useRef } from "react";
import "./reg.css"
import useNonceGenerator from '../utils/nonce';

const PWD_REGEX = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,14}$/;
const USER_REGEX = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,14}$/;

const Register = () => {
    const userRef = useRef<HTMLInputElement | null>(null);
    const errRef = useRef<HTMLInputElement | null>(null);

    const { nonce, generateNewNonce } = useNonceGenerator();

    const [user, setUser] = useState('');
    const [validName, setValidName] = useState(false);  
    const [userFocus, setUserFocus] = useState(false);

    const [pwd, setPwd] = useState('');
    const [validPwd, setValidPwd] = useState(false);
    const [pwdFocus, setPwdFocus] = useState(false);

    const [matchPwd, setMatchPwd] = useState('');
    const [validMatch, setValidMatch] = useState(false);
    const [matchFocus, setMatchFocus] = useState(false);

    const [errMsg, setErrMsg] = useState('');
    const [success, setSuccess] = useState(Boolean);

    useEffect(() => {
        if (userRef.current) { 
            userRef.current.focus();
        }
    }, [])

    useEffect(() => {
        const result = USER_REGEX.test(user);
        console.log(result);
        console.log(user);
        setValidName(result);
    }, [user])

    useEffect(() => {
        const result = PWD_REGEX.test(pwd);
        console.log(result);
        console.log(pwd);
        setValidPwd(result);
        const match = pwd === matchPwd;
        setValidMatch(match)
    }, [pwd, matchPwd])

    useEffect(() => {
        setErrMsg('');
    }, [user, pwd, matchPwd])

    /*const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        //extra protection step
        const v1 = USER_REGEX.test(user);
        const v2 = PWD_REGEX.test(pwd);
        if (!v1 || !v2) {
            setErrMsg("Invaild Entry");
            return;
        }
        console.log(user, pwd);
        setSuccess(true);
    }
*/

    const handleSubmit =async (e: React.FormEvent) => {
        const requestOptions = {
            methods: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                'username': user,
                'password': pwd,
                nonce: nonce,
            })
            console.log(user,pwd,nonce)
        }
    }

    return (
        <>
        {success ? (
            <section>
                <h1>Success!</h1>
                <p>
                    <a href="#">Sign in</a>
                </p>
            </section>
        ) : ( 
        <section>
            <p ref={errRef} className={errMsg ? 'errmsg' : 'offscreen'} aria-live="assertive">{errMsg}</p>
            <h1>Register</h1>
            <form>
                <label htmlFor="username">
                    Username:
                </label>
                <input  
                    type="text"
                    id="username"
                    ref={userRef}
                    autoComplete="off"
                    onChange={(e) => setUser(e.target.value)}
                    required
                    aria-invalid={validName ? "false" : "true"}
                    aria-describedby="uidnote"
                    onFocus={() => setUserFocus(true)}
                    onBlur={() => setUserFocus(false)}
                    />
                    <p id="'uidnote" className={userFocus && user && !validName ? "instruction" : "offscreen"}>
                        stufffffff
                    </p>

                <label htmlFor="password">
                    Password:
                <span className={validPwd ? "valid" : "hide"}>
                    <i>&#10003;</i>
                </span>
                <span className={validPwd || !pwd ? "hide" : "invalid"}>
                    <i>&#215;</i>
                </span>

                </label>
                <input  
                    type="password"
                    id="password"
                    onChange={(e) => setPwd(e.target.value)}
                    required
                    aria-invalid={validPwd ? "false" : "true"}
                    aria-describedby="pwdnote"
                    onFocus={() => setPwdFocus(true)}
                    onBlur={() => setPwdFocus(false)}
                    />
                    <p id="'uidnote" className={pwdFocus && !validPwd ? "instruction" : "offscreen"}>
                        stufffffff
                    </p>

                <label htmlFor="confirm_pwd">
                    Confirm Password:
                <span className={validMatch && matchPwd ? "valid" : "hide"}>
                    <i>&#10003;</i>
                </span>
                <span className={validMatch || !matchPwd ? "hide" : "invalid"}>
                    <i>&#215;</i>
                </span>

                </label>
                <input  
                    type="password"
                    id="confirm_pwd"
                    onChange={(e) => setMatchPwd(e.target.value)}
                    required
                    aria-invalid={validMatch ? "false" : "true"}
                    aria-describedby="confirmnote"
                    onFocus={() => setMatchFocus(true)}
                    onBlur={() => setMatchFocus(false)}
                    />
                    <p id="'uidnote" className={matchFocus && !validMatch ? "instruction" : "offscreen"}>
                        stufffffff
                    </p>

                    <button disabled={!validName || !validPwd || !validMatch ? true : false}>Sign Up</button>
            </form>
            <p>
                Already registered?<br />
                <span className="line">
                    {/*put router link here*/}
                    <a href="#">Sign In</a>
                </span>
            </p>

        </section>
        )}
        </>
    )
}

export default Register