export const isAuthenticated = (): boolean => {
    const token = localStorage.getItem("token");
    return !!token;
  };
  
  export const getToken = (): string | null => {
    return localStorage.getItem("token");
  };
  
  export const logout = (): void => {
    localStorage.removeItem("token");
    window.location.href = "/";
  };
  