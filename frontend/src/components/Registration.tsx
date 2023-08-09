import React from 'react';
import useRegistration, { UserRegistrationData } from '../hooks/useRegistration'

function RegistrationComponent() {
  const { registerUser, response, error, isLoading } = useRegistration();

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    const userData: UserRegistrationData = {
      //username: 'exampleuser',
      email: 'user@example.com',
      password: 'securepassword',
      confirmPassword: 'confirmpassword',
      // Other user data
    };

    registerUser(userData);
  };

  return (
    <div>
      <h2>User Registration</h2>
      <form onSubmit={handleSubmit}>
        {/* Input fields for user data */}
        <button type="submit" disabled={isLoading}>
          Register
        </button>
      </form>

      {isLoading && <p>Loading...</p>}
      {error && <p>Error: {error}</p>}
      {response && <p>Registration Successful: {response.message}</p>}
    </div>
  );
}

export default RegistrationComponent;
