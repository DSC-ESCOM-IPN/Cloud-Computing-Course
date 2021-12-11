import axios from 'axios';

export const getProfile = (boleta) => {
    return axios
        .get(
            `/api/psql/${boleta}`,
            {
                headers: { "Content-type": "application/json" }
            }).then(res => {
                console.log(res);
                return res.data;
            })
}

export const getProfiles = () => {
    return axios
        .get(
            `/api/psql/`,
            {
                headers: { "Content-type": "application/json" }
            }).then(res => {
                console.log(res);
                return res.data;
            })
}