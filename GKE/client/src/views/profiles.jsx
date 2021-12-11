import React, { useEffect } from 'react';
import { getProfiles } from '../utils/functions';
import ProfilesTable from '../components/ProfilesTable';
import { Typography } from '@mui/material';

export default function Profiles() {
    const [profiles, setProfiles] = React.useState([]);

    useEffect(() => {
        getProfiles().then((res) => {
            console.log(res);
            setProfiles(res)
        });
    }, []);

    return (
        profiles ?
            <div>
                <Typography variant='h1'> Profiles </Typography>
                <ProfilesTable data={profiles} />
            </div>
            : <Typography> Loading... </Typography>
    );
}