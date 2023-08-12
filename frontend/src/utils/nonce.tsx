import { useEffect, useState } from 'react';
import { SHA256, enc } from 'crypto-js';

const useNonce = (sizeInBytes: number = 12) => {
  const [nonce, setNonce] = useState<string>('');

  useEffect(() => {
    // Generate a new nonce when the component mounts
    generateNonce(sizeInBytes);
  }, []);

  const generateNonce = (size: number) => {
    const nonceBytes = generateRandomBytes(size);
    const newNonce = bytesToHex(nonceBytes); // Convert nonceBytes to a hexadecimal string
    setNonce(newNonce);
  };

  const generateRandomBytes = (sizeInBytes: number) => {
    const randomBytes = new Uint8Array(sizeInBytes);
    for (let i = 0; i < sizeInBytes; i++) {
      randomBytes[i] = Math.floor(Math.random() * 256);
    }
    return randomBytes;
  };

  const bytesToHex = (bytes: Uint8Array) => {
    return Array.from(bytes)
      .map((byte) => byte.toString(16).padStart(2, '0'))
      .join('');
  };

  const regenerateNonce = () => {
    generateNonce(sizeInBytes);
  };

  return { nonce, regenerateNonce };
};

export default useNonce;
