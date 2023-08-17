import React, { useEffect, useState, useRef } from "react";
import "./reg.css"
import useSubmit from "../utils/useSubmit";

const PWD_REGEX = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,14}$/;
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;


const Register = () => {
    const { response, error, isLoading, performSubmit } = useSubmit();

    const emailRef = useRef<HTMLInputElement | null>(null);
    const errRef = useRef<HTMLInputElement | null>(null);

    const [email, setemail] = useState('');
    const [validName, setValidName] = useState(false);  
    const [emailFocus, setemailFocus] = useState(false);

    const [pwd, setPwd] = useState('');
    const [validPwd, setValidPwd] = useState(false);
    const [pwdFocus, setPwdFocus] = useState(false);

    const [matchPwd, setMatchPwd] = useState('');
    const [validMatch, setValidMatch] = useState(false);
    const [matchFocus, setMatchFocus] = useState(false);

    const [errMsg, setErrMsg] = useState('');
    const [success, setSuccess] = useState(Boolean);

    useEffect(() => {
        if (emailRef.current) { 
            emailRef.current.focus();
        }
    }, [])

    useEffect(() => {
        const result = EMAIL_REGEX.test(email);
        console.log(result);
        console.log(email);
        setValidName(result);
    }, [email])

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
    }, [email, pwd, matchPwd])

    /*const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        //extra protection step
        const v1 = email_REGEX.test(email);
        const v2 = PWD_REGEX.test(pwd);
        if (!v1 || !v2) {
            setErrMsg("Invaild Entry");
            return;
        }
        console.log(email, pwd);
        setSuccess(true);
    }
*/

    const handleSubmit =async (e: React.FormEvent): Promise<void> => {
        e.preventDefault;
        const formData = {
            'email': email,
            'password': pwd
        };
        await performSubmit('http://localhost:5000/', 'POST', formData);
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
                <label htmlFor="email">
                    email:
                </label>
                <input  
                    type="text"
                    id="emailname"
                    ref={emailRef}
                    autoComplete="off"
                    onChange={(e) => setemail(e.target.value)}
                    required
                    aria-invalid={validName ? "false" : "true"}
                    aria-describedby="uidnote"
                    onFocus={() => setemailFocus(true)}
                    onBlur={() => setemailFocus(false)}
                    />
                    <p id="'uidnote" className={emailFocus && email && !validName ? "instruction" : "offscreen"}>
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