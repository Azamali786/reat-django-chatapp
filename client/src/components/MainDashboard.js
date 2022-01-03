import React from 'react';
import ChatGroups from './ChatGroups';
import ChatDashboard from './ChatDashboard';
import UserStatus from './UserStatus';
import Button from './Button';


const MainDashboard = () => {
    return (
        <div className="App">
            <header className="App-header">
                <Button />
                <ChatGroups /> 
                <ChatDashboard />
                <UserStatus />
            </header>
        </div>
    )
}

export default MainDashboard
