import { useState } from 'react';

interface ApiResponse {
  message: string;
  // Other response data properties
}

export interface UserRegistrationData {
  username: string;
  email: string;
  password: string;
  // Other user data properties
}

interface RegistrationHookResult {
  registerUser: (userData: UserRegistrationData) => Promise<void>;
  response: ApiResponse | null;
  error: string | null;
  isLoading: boolean;
}

function useRegistration(): RegistrationHookResult {
  const [response, setResponse] = useState<ApiResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const registerUser = async (userData: UserRegistrationData) => {
    setIsLoading(true);
    setError(null);  //this is not needed?

    try {
      const response = await fetch('/auth/registration', {  //check paths
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',  //not needed?
        },
        body: JSON.stringify(userData),  //make sure api accepts this
      });

      const responseData: ApiResponse = await response.json();  //get route to send success?
      setResponse(responseData);
    } catch (error) {
      setError('An error occurred while registering.');
    } finally {
      setIsLoading(false);
    }
  };

  return {
    registerUser,
    response,
    error,
    isLoading,
  };
}

export default useRegistration;
