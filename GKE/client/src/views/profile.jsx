import React, { useEffect } from 'react';
import { useParams } from 'react-router';
import { getProfile } from '../utils/functions';
import ProfileCard from '../components/ProfileCard';
import { Typography } from '@mui/material';

export default function Profile() {
    const { boleta } = useParams();
    const [profile, setProfile] = React.useState(null);

    useEffect(() => {
        getProfile(boleta).then((res) => {
            console.log(res);
            setProfile(res)
        });
    }, [boleta]);

    return (
        profile ? <ProfileCard Profile={profile} /> : <Typography> Not found</Typography>
    );
}