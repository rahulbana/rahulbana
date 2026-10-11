// ---------------------------------------------------------------------------
// Name:     Rahul Singh Bana
// Email:    bana.saa@gmail.com
// LinkedIn: https://www.linkedin.com/in/rahulsinghbana
// Repo:     https://github.com/rahulbana/rahulbana
// ---------------------------------------------------------------------------
import { Center, Loader } from "@mantine/core";
import { Navigate, Outlet } from "react-router-dom";

import { useAuth } from "./AuthContext";

export function ProtectedRoute() {
  const { user, loading } = useAuth();

  if (loading) {
    return (
      <Center h="100vh">
        <Loader />
      </Center>
    );
  }

  if (!user) return <Navigate to="/login" replace />;

  return <Outlet />;
}
