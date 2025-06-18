import React, { useState, useEffect } from 'react';
import './App.css';
import UserTable from './components/UserTable';
import UserModal from './components/UserModal';
import { User } from './types/User';
import { userService } from './services/userService';

function App() {
  const [users, setUsers] = useState<User[]>([]);
  const [selectedUser, setSelectedUser] = useState<User | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      setLoading(true);
      setError(null);
      const userData = await userService.getUsers();
      setUsers(userData);
    } catch (err) {
      setError('Failed to fetch users. Please try again later.');
      console.error('Error fetching users:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleUserClick = (user: User) => {
    setSelectedUser(user);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setSelectedUser(null);
  };

  const handleDeleteUser = async (userId: number) => {
    try {
      await userService.deleteUser(userId);
      setUsers(users.filter(user => user.id !== userId));
    } catch (err) {
      console.error('Error deleting user:', err);
      // Note: Since this is client-side only as per requirements, 
      // we still remove from local state even if API call fails
      setUsers(users.filter(user => user.id !== userId));
    }
  };

  if (loading) {
    return (
      <div className="app">
        <div className="loading-container">
          <div className="loading-spinner"></div>
          <p>Loading users...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="app">
        <div className="error-container">
          <h2>Error</h2>
          <p>{error}</p>
          <button onClick={fetchUsers} className="retry-button">
            Try Again
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>User Directory</h1>
        <p>Manage and view user information from JSONPlaceholder API</p>
      </header>
      
      <main className="app-main">
        <UserTable 
          users={users}
          onUserClick={handleUserClick}
          onDeleteUser={handleDeleteUser}
        />
      </main>

      <UserModal
        user={selectedUser}
        isOpen={isModalOpen}
        onClose={handleCloseModal}
      />
    </div>
  );
}

export default App;
