import { useState } from 'react';

interface ApiResponse {
  message: string; // Adjust this to match the response structure
}

type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE' | 'OPTIONS'; // Define the HttpMethod type

interface UseSubmitHook {
  response: ApiResponse | null;
  error: Error | null;
  isLoading: boolean;
  performSubmit: (url: string, method: HttpMethod, data: object) => Promise<void>;
}

const useSubmit = (): UseSubmitHook => {
  const [response, setResponse] = useState<ApiResponse | null>(null);
  const [error, setError] = useState<Error | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const performSubmit = async (
    url: string,
    method: HttpMethod,
    data: object
  ): Promise<void> => {
    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch(url, {
        method: method,
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      const responseData: ApiResponse = await response.json();
      setResponse(responseData);
    } catch (error) {
      if (error instanceof Error) {
        setError(error);
      }
    } finally {
      setIsLoading(false);
    }
  };

  return { response, error, isLoading, performSubmit };
};

export default useSubmit;
