import crypto from 'crypto';
import { useCallback, useState } from 'react';

interface NonceGeneratorHook {
  nonce: string;
  generateNewNonce: () => void;
}

const useNonceGenerator = (sizeInBytes = 12): NonceGeneratorHook => {
  const [nonce, setNonce] = useState<string>(generateNonce(sizeInBytes));

  const generateNewNonce = useCallback((): void => {
    setNonce(generateNonce(sizeInBytes));
  }, [sizeInBytes]);

  return { nonce, generateNewNonce };
};

const generateNonce = (sizeInBytes: number): string => {
  const nonceBytes = crypto.randomBytes(sizeInBytes);
  return nonceBytes.toString('hex');
};

export default useNonceGenerator;
