import axios from 'axios';

const BASE_URL = 'http://http://127.0.0.1:5000/api';

const api = axios.create({
  baseURL: BASE_URL,
});

export const fetchUsers = () => api.get('/users');
export const fetchUser = (userId) => api.get(`/user/${userId}`);

export const fetchAuthorizations = () => api.get('/authorizations');


export const fetchProfiles = () => api.get('/profiles');


export const fetchProducts = () => api.get('/products');
export const fetchProduct = (productId) => api.get(`/product/${productId}`);


export const fetchOrders = () => api.get('/orders');


export const fetchStores = () => api.get('/stores');


export default api;
