import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests if available
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auth API
export const authAPI = {
  register: async (email: string, password: string) => {
    const response = await api.post('/register', { email, password });
    return response.data;
  },
  
  login: async (email: string, password: string) => {
    const formData = new URLSearchParams();
    formData.append('username', email);
    formData.append('password', password);
    
    const response = await api.post('/login', formData, {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    });
    return response.data;
  },
  
  getMe: async () => {
    const response = await api.get('/me');
    return response.data;
  },
};

// Workspace API
export const workspaceAPI = {
  create: async (name: string) => {
    const response = await api.post('/workspace/create', { name });
    return response.data;
  },
  
  getAll: async () => {
    const response = await api.get('/workspace/my');
    return response.data;
  },
};

// Papers API
export const papersAPI = {
  search: async (query: string) => {
    const response = await api.get(`/papers/search?query=${encodeURIComponent(query)}`);
    return response.data;
  },
};

// Chat API
export const chatAPI = {
  sendMessage: async (message: string) => {
    const response = await api.post('/chat/chat', { content: message });
    return response.data;
  },
};

export default api;

