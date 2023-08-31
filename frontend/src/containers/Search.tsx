import React, { useState } from "react";
import useSubmit from "../utils/useSubmit";
import Card from "../components/Card";

const DataFetching = () => {
    const { response, error, isLoading, performSubmit } = useSubmit();

    const [data, setData] = useState([]); //equivalent to response??

    const handleSubmit =async (e: React.FormEvent): Promise<void> => {
        e.preventDefault;
        const formData = {
            //add params
        };
        await performSubmit('http://127.0.0.1:5000/', 'GET', formData);
        console.log(formData);
    }
}

const Search = () => {
    
}