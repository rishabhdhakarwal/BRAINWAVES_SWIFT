import axios from 'axios';
const API_URL = 'http://localhost:8000';


export default class StocksService{

    constructor(){}


    getClient() {
        const url = `${API_URL}/client/`;
        return axios.get(url).then(response => response.data);
    }  
    
    getSG() {
    	const url = `${API_URL}/sg/`;
        return axios.get(url).then(response => response.data);
	}
	getStatus(){
        const url = `${API_URL}/status/`;
        return axios.get(url).then(response => response.data);
    }
	


}