import crypto from "crypto"
import { useCallback, useState } from "react"



const useNonceGenerator = (sizeInBytes = 12) => {
    const [nonce, setNonce] = useState(generateNonce(sizeInBytes));

    const generateNewNonce = useCallback(() => {
        setNonce(generateNewNonce(sizeInBytes));
    }, [sizeInBytes]);
    return { nonce, generateNewNonce };
};

const generateNonce = (sizeInBytes) => {
    const nonceBytes = crypto.randomBytes(sizeInBytes);
    return nonceBytes.toString('hex');
};

export default useNonceGenerator;