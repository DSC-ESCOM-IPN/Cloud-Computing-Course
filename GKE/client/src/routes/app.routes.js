import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Profile from '../views/profile';
import Profiles from '../views/profiles';

const AppRoutes = () => (
    <div>
        <Routes>
            <Route exact path='/' element={<Navigate to='/profiles' />} />
            <Route exact path="/profiles" element={<Profiles />} />
            <Route exact path="/profile/:boleta" element={<Profile />} />
        </Routes>
    </div>
);

export default AppRoutes;