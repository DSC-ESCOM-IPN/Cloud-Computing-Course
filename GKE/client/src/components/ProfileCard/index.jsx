import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

export default function ProfileCard({ profile }) {
    return (
        <Box sx={{ minWidth: 275 }}>
            <Card variant="outlined">
                <React.Fragment>
                    <CardContent>
                        <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                            {profile['boleta']}
                        </Typography>
                        <Typography variant="h5" component="div">
                            {profile['firstname']}
                        </Typography>
                        <Typography sx={{ mb: 1.5 }} color="text.secondary">
                            {profile['lastname']}
                        </Typography>
                    </CardContent>
                </React.Fragment>
            </Card>
        </Box>
    );
}
