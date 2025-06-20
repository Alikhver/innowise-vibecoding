import React from "react";
import { User } from "../types/User";
import styles from "./UserModal.module.css";

interface UserModalProps {
  user: User | null;
  isOpen: boolean;
  onClose: () => void;
}

const UserModal: React.FC<UserModalProps> = ({ user, isOpen, onClose }) => {
  if (!isOpen || !user) return null;

  const handleMapClick = () => {
    const { lat, lng } = user.address.geo;
    window.open(`https://www.google.com/maps?q=${lat},${lng}`, "_blank");
  };

  return (
    <div className={styles["modal-overlay"]} onClick={onClose}>
      <div className={styles["modal-content"]} onClick={(e) => e.stopPropagation()}>
        <div className={styles["modal-header"]}>
          <h2>User Details</h2>
          <button className={styles["close-button"]} onClick={onClose}>
            ×
          </button>
        </div>
        <div className={styles["modal-body"]}>
          <div className={styles["user-info"]}>
            <div className={styles["info-section"]}>
              <h3>Personal Information</h3>
              <p><strong>Name:</strong> {user.name}</p>
              <p><strong>Username:</strong> {user.username}</p>
              <p><strong>Email:</strong> {user.email}</p>
              <p><strong>Phone:</strong> {user.phone}</p>
              <p><strong>Website:</strong> <a href={`https://${user.website}`} target="_blank" rel="noopener noreferrer">{user.website}</a></p>
            </div>
            <div className={styles["info-section"]}>
              <h3>Address</h3>
              <p><strong>Street:</strong> {user.address.street}</p>
              <p><strong>Suite:</strong> {user.address.suite}</p>
              <p><strong>City:</strong> {user.address.city}</p>
              <p><strong>Zipcode:</strong> {user.address.zipcode}</p>
              <button className={styles["map-button"]} onClick={handleMapClick}>
                View on Map
              </button>
            </div>
            <div className={styles["info-section"]}>
              <h3>Company</h3>
              <p><strong>Name:</strong> {user.company.name}</p>
              <p><strong>Catch Phrase:</strong> {user.company.catchPhrase}</p>
              <p><strong>Business:</strong> {user.company.bs}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default UserModal;
