const checkUserToken = () => {
  const userToken = localStorage.getItem('user-token');
  if (!userToken || userToken === 'undefined') {
      setIsLoggedIn(false);
      return navigate('/auth/login');
  }
  setIsLoggedIn(true);
}