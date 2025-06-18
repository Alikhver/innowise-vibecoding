# User Directory Application

A modern, responsive React TypeScript application that displays and manages user data from the JSONPlaceholder API. This application provides a professional user interface with a table-like layout and modal interaction for user details.

## Features

### Core Functionality
- **User List Display**: Table-like layout showing user information with columns for name/email, address, phone, website, and company name
- **User Detail Modal**: Detailed user information display with organized sections for personal info, address, and company details
- **User Management**: Client-side user deletion with confirmation dialogs
- **Map Integration**: Direct links to Google Maps using user geo coordinates

### Technical Features
- **Responsive Design**: Optimized for different screen sizes with mobile-first approach
- **Modern UI/UX**: Clean interface with smooth animations and hover effects
- **TypeScript**: Full type safety with comprehensive interfaces
- **CSS Modules**: Scoped styling for maintainable and modular CSS
- **Error Handling**: Graceful error handling with retry functionality
- **Loading States**: Professional loading indicators and states

## Technology Stack

- **React 18** with TypeScript
- **CSS Modules** for styling
- **JSONPlaceholder API** for test data
- **Modern ES6+** JavaScript features
- **Responsive Design** with CSS Grid and Flexbox

## Project Structure

```
src/
├── components/
│   ├── UserTable.tsx          # Main table component
│   ├── UserTable.module.css   # Table styling
│   ├── UserModal.tsx          # Modal component
│   └── UserModal.module.css   # Modal styling
├── services/
│   └── userService.ts         # API service layer
├── types/
│   └── User.ts               # TypeScript interfaces
├── App.tsx                   # Main application component
├── App.css                   # Global application styles
└── index.tsx                 # Application entry point
```

## Data Structure

The application uses the following TypeScript interfaces:

```typescript
interface Geo {
  lat: string;
  lng: string;
}

interface Address {
  street: string;
  suite: string;
  city: string;
  zipcode: string;
  geo: Geo;
}

interface Company {
  name: string;
  catchPhrase: string;
  bs: string;
}

interface User {
  id: number;
  name: string;
  username: string;
  email: string;
  address: Address;
  phone: string;
  website: string;
  company: Company;
}
```

## Getting Started

### Prerequisites
- Node.js (version 14 or higher)
- npm or yarn package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd user-directory
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

4. Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

### Available Scripts

- `npm start` - Runs the app in development mode
- `npm test` - Launches the test runner
- `npm run build` - Builds the app for production
- `npm run eject` - Ejects from Create React App (one-way operation)

## API Integration

The application integrates with the JSONPlaceholder API:

- **Base URL**: `https://jsonplaceholder.typicode.com`
- **Endpoint**: `/users` - Fetches all users
- **Delete Endpoint**: `/users/{id}` - Deletes a specific user (client-side only)

## User Interface

### Main Table
- Displays users in a responsive table format
- Columns: Name/Email, Address, Phone, Website, Company, Actions
- Clickable rows to open user details
- Delete buttons with confirmation dialogs
- Hover effects and visual feedback

### User Modal
- Comprehensive user information display
- Organized sections: Personal Information, Address, Company
- Map integration with Google Maps
- Smooth animations and transitions
- Responsive design for mobile devices

## Styling Approach

The application uses CSS Modules for component-scoped styling:

- **Global Styles**: App.css for application-wide styling
- **Component Styles**: Individual .module.css files for each component
- **Responsive Design**: Mobile-first approach with breakpoints
- **Modern CSS**: Flexbox, Grid, animations, and transitions

## Error Handling

- Network error handling with user-friendly messages
- Loading states with professional spinners
- Retry functionality for failed API calls
- Graceful degradation for missing data

## Performance Considerations

- Efficient re-rendering with React hooks
- Optimized API calls with proper error handling
- Responsive images and lazy loading ready
- Minimal bundle size with modern build tools

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Acknowledgments

- JSONPlaceholder for providing the test API
- Create React App for the development setup
- React community for excellent documentation and tools 